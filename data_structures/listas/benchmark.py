class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # Apunta al siguiente nodo
        
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Acceso a un elemento en una Lista Enlazada
    # Método iterativo
    def acceder_iterativo(self, index):
        actual = self.cabeza
        contador = 0
        while actual:
            if contador == index:
                return actual.valor
            actual = actual.siguiente
            contador += 1
        return None  # Índice fuera de rango

    # Método recursivo
    def acceder_recursivo(self, nodo, index):
        if not nodo:  
            return None  # Caso base: índice fuera de rango
        if index == 0:
            return nodo.valor  # Caso base: encontramos el nodo
        return self.acceder_recursivo(nodo.siguiente, index - 1)  # Llamada recursiva

    # Insertamos un valor en una posición específica.
    # Método iterativo
    def insertar_iterativo(self, index, valor):
        nuevo_nodo = Nodo(valor)
        if index == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        contador = 0
        while actual and contador < index - 1:
            actual = actual.siguiente
            contador += 1
        if not actual:
            return  # Índice inválido
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo

    # Método recursivo
    def insertar_recursivo(self, nodo, index, valor):
        if index == 0:
            nuevo_nodo = Nodo(valor)
            nuevo_nodo.siguiente = nodo
            return nuevo_nodo
        if not nodo:
            return None  # Índice inválido
        nodo.siguiente = self.insertar_recursivo(nodo.siguiente, index - 1, valor)
        return nodo
    
import time

# Creamos una lista con 1000 elementos
lista = ListaEnlazada()
for i in range(1000):
    lista.insertar_iterativo(i, i)

# Medimos acceso iterativo
start = time.time()
lista.acceder_iterativo(500)
end = time.time()
print(f"Tiempo acceso iterativo: {end - start:.6f} segundos")

# Medimos acceso recursivo
start = time.time()
lista.acceder_recursivo(lista.cabeza, 500)
end = time.time()
print(f"Tiempo acceso recursivo: {end - start:.6f} segundos")

# Medimos inserción iterativa
start = time.time()
lista.insertar_iterativo(500, 9999)
end = time.time()
print(f"Tiempo inserción iterativa: {end - start:.6f} segundos")

# Medimos inserción recursiva
start = time.time()
lista.cabeza = lista.insertar_recursivo(lista.cabeza, 500, 9999)
end = time.time()
print(f"Tiempo inserción recursiva: {end - start:.6f} segundos")
