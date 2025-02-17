import time
import random
import matplotlib.pyplot as plt

# Algoritmos de ordenamiento

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Función para medir tiempos
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

# Tamaños de prueba
sizes = [100, 500, 1000, 5000, 10000]
bubble_times, merge_times, quick_times, heap_times = [], [], [], []

for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]
    bubble_times.append(measure_time(bubble_sort, arr.copy()))
    merge_times.append(measure_time(merge_sort, arr.copy()))
    quick_times.append(measure_time(quick_sort, arr.copy()))
    heap_times.append(measure_time(heap_sort, arr.copy()))

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, label="Bubble Sort", marker="o")
plt.plot(sizes, merge_times, label="Merge Sort", marker="s")
plt.plot(sizes, quick_times, label="Quick Sort", marker="^")
plt.plot(sizes, heap_times, label="Heap Sort", marker="d")

plt.xlabel("Tamaño del array")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.title("Comparación de Algoritmos de Ordenamiento")
plt.legend()
plt.grid()
plt.show()
