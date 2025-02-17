import time
import numpy as np
import matplotlib.pyplot as plt

# Tamaños de array a evaluar
tamaños = np.logspace(1, 6, num=10, dtype=int)
tiempos_acceso = []
tiempos_insercion = []

for size in tamaños:
    arr = list(range(size))
    
    # Medir tiempo de acceso
    start = time.time()
    _ = arr[size // 2]  # Acceso a un elemento central
    tiempos_acceso.append(time.time() - start)
    
    # Medir tiempo de inserción
    start = time.time()
    arr.insert(size // 2, -1)  # Insertar en el medio
    tiempos_insercion.append(time.time() - start)

# Graficar resultados
plt.figure(figsize=(8, 5))
plt.plot(tamaños, tiempos_acceso, label='Acceso (O(1))', marker='o')
plt.plot(tamaños, tiempos_insercion, label='Inserción en medio (O(n))', marker='s')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Tamaño del Array')
plt.ylabel('Tiempo (s)')
plt.title('Comparación de Acceso vs. Inserción en Arrays')
plt.legend()
plt.grid(True)
plt.show()
