# Se usan listas auxiliares (left, middle, right), lo que hace la implementación clara
# pero menos eficiente en consumo de memoria.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Se elige el pivote en la mitad
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print(quick_sort(arr))
