# Python usa un Heap Mínimo, por lo que extrae los elementos en orden ascendente.
# Menos código pero menos control sobre el heap.

import heapq

def heap_sort_lib(arr):
    heapq.heapify(arr)  # Convierte la lista en un heap mínimo
    return [heapq.heappop(arr) for _ in range(len(arr))]  # Extrae elementos en orden

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print(heap_sort_lib(arr))
