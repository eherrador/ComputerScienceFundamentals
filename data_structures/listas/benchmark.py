import time
import matplotlib.pyplot as plt
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

# 🔥 Prueba de rendimiento
tamanios = [100, 500, 1000, 5000, 10000]
tiempos_acceso_iter = []
tiempos_acceso_recur = []
tiempos_insert_iter = []
tiempos_insert_recur = []

# Creamos una lista
for n in tamanios:
    lista = ListaEnlazada()
    for i in range(n):
        lista.insertar_iterativo(i, i)

    # Medimos acceso iterativo
    start = time.time()
    lista.acceder_iterativo(500)
    end = time.time()
    tiempos_acceso_iter.append(end - start)

    # Medimos acceso recursivo
    start = time.time()
    lista.acceder_recursivo(lista.cabeza, 500)
    end = time.time()
    tiempos_acceso_recur.append(end - start)

    # Medimos inserción iterativa
    start = time.time()
    lista.insertar_iterativo(500, 9999)
    end = time.time()
    tiempos_insert_iter.append(end - start)

    # Medimos inserción recursiva
    start = time.time()
    lista.cabeza = lista.insertar_recursivo(lista.cabeza, 500, 9999)
    end = time.time()
    tiempos_insert_recur.append(end - start)

print(f"Tamaños probados: {tamanios}")
print(f"Tiempos Acceso Iterativo: {tiempos_acceso_iter}")
print(f"Tiempos Acceso Recursivo: {tiempos_acceso_recur}")
print(f"Tiempos Inserción Iterativa: {tiempos_insert_iter}")
print(f"Tiempos Inserción Recursiva: {tiempos_insert_recur}")

# 📊 Generar gráfico
plt.figure(figsize=(10, 5))

# Gráfico de acceso
plt.subplot(1, 2, 1)
plt.plot(tamanios, tiempos_acceso_iter, label="Acceso Iterativo", marker="o")
plt.plot(tamanios, tiempos_acceso_recur, label="Acceso Recursivo", marker="s")
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (s)")
plt.title("Tiempo de Acceso")
plt.legend()
plt.grid()

# Gráfico de inserción
plt.subplot(1, 2, 2)
plt.plot(tamanios, tiempos_insert_iter, label="Inserción Iterativa", marker="o")
plt.plot(tamanios, tiempos_insert_recur, label="Inserción Recursiva", marker="s")
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (s)")
plt.title("Tiempo de Inserción")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()