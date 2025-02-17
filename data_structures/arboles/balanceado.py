class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Se usa para balancear el árbol

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Rotación
        y.right = z
        z.left = T3

        # Actualizar alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Rotación
        y.left = z
        z.right = T2

        # Actualizar alturas
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        # Actualizar altura
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Obtener balance
        balance = self.get_balance(node)

        # Caso Izquierda-Izquierda (Rotación Derecha)
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)

        # Caso Derecha-Derecha (Rotación Izquierda)
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)

        # Caso Izquierda-Derecha (Rotación Izquierda-Derecha)
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Caso Derecha-Izquierda (Rotación Derecha-Izquierda)
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def print_tree(self, node, level=0, prefix="Root: "):
        """Imprime el árbol de manera estructurada"""
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

# Ejemplo de uso
avl = AVLTree()
root = None

# Insertar valores
for value in [10, 20, 30, 40, 50, 25]:
    root = avl.insert(root, value)
    avl.print_tree(root)

# Imprimir recorrido en preorden
print("Árbol después del balanceo:")
avl.print_tree(root)
print("Preorden después del balanceo:")
avl.preorder_traversal(root)  # Salida esperada: 30 20 10 25 40 50
