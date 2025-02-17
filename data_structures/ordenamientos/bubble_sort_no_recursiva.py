# Se usa la variable swapped para detener el algoritmo,
# si la lista ya está ordenada antes de completar todas las iteraciones.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  # Intercambio si están desordenados
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Si no hubo intercambios, la lista ya está ordenada
            break
    return arr

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
