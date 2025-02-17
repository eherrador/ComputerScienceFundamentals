class NodoCircular:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, valor):
        nuevo_nodo = NodoCircular(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza  # Apunta a sí mismo
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:  # Llegar al último nodo
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def insertar_al_final(self, valor):
        nuevo_nodo = NodoCircular(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza  # Apunta a sí mismo
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:  # Llegar al último nodo
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

    def eliminar(self, valor):
        if not self.cabeza:
            return False  # Lista vacía
        
        actual = self.cabeza
        previo = None

        while True:
            if actual.valor == valor:
                if previo:  # Nodo intermedio o final
                    previo.siguiente = actual.siguiente
                else:  # Nodo a eliminar es la cabeza
                    if actual.siguiente == self.cabeza:  # Solo hay un nodo
                        self.cabeza = None
                        return True
                    else:
                        temp = self.cabeza
                        while temp.siguiente != self.cabeza:
                            temp = temp.siguiente
                        temp.siguiente = actual.siguiente
                        self.cabeza = actual.siguiente

                return True  # Nodo eliminado
            previo = actual
            actual = actual.siguiente

            if actual == self.cabeza:  # Evitar bucle infinito
                break

        return False  # No encontrado

    def recorrer(self):
        if not self.cabeza:
            print("Lista vacía")
            return

        actual = self.cabeza
        while True:
            print(actual.valor, end=" → ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("(Inicio)")

# 🚀 Prueba de la lista circular
cll = ListaCircular()
cll.insertar_al_inicio(10)
cll.insertar_al_inicio(20)
cll.insertar_al_final(30)
cll.insertar_al_final(40)

print("Recorrido de la lista:")
cll.recorrer()

print("Eliminando 20...")
cll.eliminar(20)
cll.recorrer()
