import random
import time
import csv
import matplotlib.pyplot as plt

# Sorting algorithms implementations
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def improved_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def improved_quick_sort(arr):
    if len(arr) <= 20:
        selection_sort(arr)
    elif len(arr) > 1:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        improved_quick_sort(left)
        improved_quick_sort(right)
        arr[:] = left + middle + right

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Helper functions
def generate_random_list(size):
    return [random.randint(0, size) for _ in range(size)]

def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    end_time = time.time()
    return end_time - start_time

# Determine maximum input size for each algorithm within 2 seconds
algorithms = {
    'BubbleSort': bubble_sort,
    'Improved BubbleSort': improved_bubble_sort,
    'SelectionSort': selection_sort,
    'QuickSort': quick_sort,
    'Improved QuickSort': improved_quick_sort,
    'MergeSort': merge_sort
}

max_time = 2.0  # Maximum time in seconds
results = {}

for alg, func in algorithms.items():
    size = 10  # Start with a small size
    max_size = 0

    while True:
        input_list = generate_random_list(size)
        time_taken = measure_time(func, input_list)
        if time_taken > max_time:
            break
        max_size = size
        size *= 2  # Exponentially increase size for quicker results

    results[alg] = max_size
    print(f"{alg} can sort up to {max_size} elements within {max_time} seconds")

# Save results to CSV
with open('max_sizes_within_2_seconds_random.csv', 'w', newline='') as csvfile:
    fieldnames = ['Algorithm', 'Max Size']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for alg, max_size in results.items():
        writer.writerow({'Algorithm': alg, 'Max Size': max_size})

# Plotting the results
algorithms_list = list(results.keys())
max_sizes = list(results.values())

plt.barh(algorithms_list, max_sizes)
plt.xlabel('Maximum Input Size')
plt.ylabel('Algorithm')
plt.title('Maximum Input Size Each Algorithm Can Sort Within 2 Seconds (Random Inputs)')
plt.grid(True)
plt.savefig('max_sizes_within_2_seconds_random.png')
plt.show()

