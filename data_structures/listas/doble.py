class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_inicio(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_al_final(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if not self.cola:  # Si la lista está vacía
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente  # Si es el primer nodo

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior  # Si es el último nodo
                
                return True  # Nodo eliminado
            actual = actual.siguiente
        return False  # No encontrado

    def recorrer_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" ⇄ ")
            actual = actual.siguiente
        print("None")

    def recorrer_atras(self):
        actual = self.cola
        while actual:
            print(actual.valor, end=" ⇄ ")
            actual = actual.anterior
        print("None")

# 🚀 Prueba de la lista
dll = ListaDoblementeEnlazada()
dll.insertar_al_inicio(10)
dll.insertar_al_inicio(20)
dll.insertar_al_final(30)
dll.insertar_al_final(40)

print("Recorrido hacia adelante:")
dll.recorrer_adelante()

print("Recorrido hacia atrás:")
dll.recorrer_atras()

print("Eliminando 20...")
dll.eliminar(20)
dll.recorrer_adelante()
