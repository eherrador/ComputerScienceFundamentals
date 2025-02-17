class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # Apunta al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Primer nodo de la lista

    def insertar_inicio(self, valor):
        """Inserta un nodo al inicio de la lista"""
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def insertar_final(self, valor):
        """Inserta un nodo al final de la lista"""
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar(self, valor):
        """Elimina el primer nodo con el valor dado"""
        actual = self.cabeza
        if actual and actual.valor == valor:
            self.cabeza = actual.siguiente
            return
        anterior = None
        while actual and actual.valor != valor:
            anterior = actual
            actual = actual.siguiente
        if actual:
            anterior.siguiente = actual.siguiente

    def buscar(self, valor):
        """Busca un valor en la lista y devuelve True si existe"""
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def imprimir(self):
        """Imprime la lista enlazada"""
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# 🔥 Prueba
lista = ListaEnlazada()
lista.insertar_inicio(3)
lista.insertar_inicio(2)
lista.insertar_inicio(1)
lista.insertar_final(4)
lista.insertar_final(5)
lista.imprimir()  # 1 -> 2 -> 3 -> 4 -> 5 -> None

lista.eliminar(3)
lista.imprimir()  # 1 -> 2 -> 4 -> 5 -> None

print(lista.buscar(4))  # True
print(lista.buscar(3))  # False
