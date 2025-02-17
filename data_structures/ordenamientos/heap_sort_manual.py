# Se construye el heap iterativamente y se extrae el máximo repetidamente.
# El heapify es recursivo, pero su llamada está dentro de un bucle.
def heap_sort(arr):
    n = len(arr)

    # Construir el heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Mover el máximo al final
        heapify(arr, i, 0)  # Restaurar la propiedad del heap

    return arr

def heapify(arr, n, i):
    largest = i  # Inicializar el nodo padre como el más grande
    left = 2 * i + 1  # Hijo izquierdo
    right = 2 * i + 2  # Hijo derecho

    # Comparar con el hijo izquierdo
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Comparar con el hijo derecho
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el nodo padre no es el más grande, intercambiar y seguir ajustando
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # Recursivamente restaurar el heap

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print(heap_sort(arr))
