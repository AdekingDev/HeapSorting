import random
def heapify(arr, n, i, counter):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        counter["ops"] += 1
        heapify(arr, n, largest, counter)

def heapSort(arr):
    n = len(arr)
    counter = {"ops": 0}

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, counter)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        counter["ops"] += 1
        heapify(arr, i, 0, counter)

    return counter["ops"]

def partition(arr, low, high, counter):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            counter["ops"] += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    counter["ops"] += 1
    return i + 1

def quickSort(arr, low, high, counter):
    if low < high:
        pi = partition(arr, low, high, counter)
        quickSort(arr, low, pi - 1, counter)
        quickSort(arr, pi + 1, high, counter)


# Create an array of 100 integers
array = [random.randint(0, 1000) for _ in range(100)]

array_for_quick_sort = array.copy()

# Applying the Heap Sort
heap_operations = heapSort(array)
print("Heap Sort:")
print(array)
print("Number of operations:", heap_operations)

# Applying the Quick Sort
quick_operations = {"ops": 0}
quickSort(array_for_quick_sort, 0, len(array_for_quick_sort) - 1, quick_operations)
print("\nQuick Sort:")
print(array_for_quick_sort)
print("Number of operations:", quick_operations["ops"])

