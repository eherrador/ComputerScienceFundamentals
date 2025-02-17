# Se fusionan sublistas de tamaño creciente hasta que todo el array esté ordenado.
def merge_sort_iterative(arr):
    width = 1
    n = len(arr)

    while width < n:
        for i in range(0, n, 2 * width):
            left = arr[i : i + width]
            right = arr[i + width : i + 2 * width]
            arr[i : i + 2 * width] = merge(left, right)
        width *= 2

    return arr

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort_iterative(arr))

