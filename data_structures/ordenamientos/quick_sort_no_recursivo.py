# Aquí evitamos la recursión usando una pila para manejar las sublistas pendientes.
# Particionamos in-place, sin crear listas adicionales, mejorando la eficiencia de memoria.

def quick_sort_iterative(arr):
    stack = [(0, len(arr) - 1)]  # Pila con los índices de las sublistas a ordenar

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue

        pivot_index = partition(arr, left, right)
        stack.append((left, pivot_index - 1))  # Sublista izquierda
        stack.append((pivot_index + 1, right))  # Sublista derecha

    return arr

def partition(arr, left, right):
    pivot = arr[right]  # Usamos el último elemento como pivote
    i = left - 1  # Índice para los elementos menores al pivote

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]  # Colocar pivote en su lugar
    return i + 1  # Retornar índice del pivote

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort_iterative(arr))
