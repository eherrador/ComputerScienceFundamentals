# La versión recursiva no es eficiente en la práctica,
# porque consume más memoria debido a las llamadas recursivas.

def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)

    if n == 1:
        return arr

    swapped = False
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:  # Intercambio si están desordenados
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True

    if not swapped:
        return arr  # Si no hubo intercambios, la lista ya está ordenada

    return bubble_sort_recursive(arr, n - 1)

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort_recursive(arr))
