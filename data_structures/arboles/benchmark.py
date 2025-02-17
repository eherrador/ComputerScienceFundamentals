import time
import random
import matplotlib.pyplot as plt

# --------------------- BST ---------------------
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert_rec(self.root, value)

    def _insert_rec(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_rec(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_rec(node.right, value)

    def search(self, value):
        return self._search_rec(self.root, value)

    def _search_rec(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_rec(node.left, value)
        return self._search_rec(node.right, value)

# --------------------- AVL ---------------------
class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, node, value):
        if not node:
            return AVLNode(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self.search(node.left, value)
        return self.search(node.right, value)

# --------------------- Comparación de Tiempos ---------------------

def measure_time(tree_type, num_elements, num_searches):
    """Mide el tiempo de inserción y búsqueda en un árbol"""
    if tree_type == "BST":
        tree = BST()
    else:
        tree = AVL()
        root = None  # AVL necesita un nodo raíz

    # Generar valores aleatorios para insertar
    values = random.sample(range(1, num_elements * 10), num_elements)

    # Medir tiempo de inserción
    start_time = time.time()
    for value in values:
        if tree_type == "BST":
            tree.insert(value)
        else:
            root = tree.insert(root, value)
    insert_time = time.time() - start_time

    # Generar valores aleatorios para buscar
    search_values = random.sample(values, num_searches)

    # Medir tiempo de búsqueda
    start_time = time.time()
    for value in search_values:
        if tree_type == "BST":
            tree.search(value)
        else:
            tree.search(root, value)
    search_time = time.time() - start_time

    return insert_time, search_time

# --------------------- Graficar Resultados ---------------------

def plot_comparison():
    sizes = [100, 500, 1000, 5000, 10000]  # Tamaños de árboles
    bst_insert_times, bst_search_times = [], []
    avl_insert_times, avl_search_times = [], []

    for size in sizes:
        bst_insert, bst_search = measure_time("BST", size, size // 2)
        avl_insert, avl_search = measure_time("AVL", size, size // 2)

        bst_insert_times.append(bst_insert)
        bst_search_times.append(bst_search)
        avl_insert_times.append(avl_insert)
        avl_search_times.append(avl_search)

    # Crear gráfica
    plt.figure(figsize=(12, 6))

    # Gráfica de inserción
    plt.subplot(1, 2, 1)
    plt.plot(sizes, bst_insert_times, label="BST Insert", marker="o", linestyle="--", color="blue")
    plt.plot(sizes, avl_insert_times, label="AVL Insert", marker="o", linestyle="-", color="red")
    plt.xlabel("Número de Elementos")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de Tiempos de Inserción")
    plt.legend()
    plt.grid(True)

    # Gráfica de búsqueda
    plt.subplot(1, 2, 2)
    plt.plot(sizes, bst_search_times, label="BST Search", marker="s", linestyle="--", color="blue")
    plt.plot(sizes, avl_search_times, label="AVL Search", marker="s", linestyle="-", color="red")
    plt.xlabel("Número de Elementos")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de Tiempos de Búsqueda")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Ejecutar la comparación
plot_comparison()
