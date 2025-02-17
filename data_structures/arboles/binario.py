# Complejidad (BST):
# Búsqueda: O(log n) en promedio, O(n) en el peor caso (si el árbol está desbalanceado).
# Inserción: O(log n) en promedio.
# Eliminación: O(log n) en promedio.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_rec(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_rec(node.right, value)

    def inorder_traversal(self, node, result=[]):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result
    
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
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(20)

tree.print_tree(tree.root)
print(tree.inorder_traversal(tree.root))  # [2, 5, 7, 10, 15]
