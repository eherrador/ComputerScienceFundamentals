class NodoDobleCircular:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDobleCircular:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, valor):
        nuevo_nodo = NodoDobleCircular(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza
            self.cabeza.anterior = self.cabeza
        else:
            cola = self.cabeza.anterior
            nuevo_nodo.siguiente = self.cabeza
            nuevo_nodo.anterior = cola
            cola.siguiente = nuevo_nodo
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def recorrer(self):
        if not self.cabeza:
            print("Lista vacía")
            return
        
        actual = self.cabeza
        while True:
            print(actual.valor, end=" ⇄ ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("(Inicio)")

# 🚀 Prueba de lista doblemente circular
cdll = ListaDobleCircular()
cdll.insertar_al_inicio(10)
cdll.insertar_al_inicio(20)
cdll.insertar_al_inicio(30)

print("Lista doblemente circular:")
cdll.recorrer()
