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

# Experimental setup
sizes = [10, 100, 1000, 10000]
#sizes = [10, 100, 1000, 10000, 100000, 1000000]
input_lists = [generate_random_list(size) for size in sizes]
algorithms = {
    'BubbleSort': bubble_sort,
    'Improved BubbleSort': improved_bubble_sort,
    'SelectionSort': selection_sort,
    'QuickSort': quick_sort,
    'Improved QuickSort': improved_quick_sort,
    'MergeSort': merge_sort
}

# Measure execution times
results = {alg: [] for alg in algorithms}
for size, input_list in zip(sizes, input_lists):
    for alg, func in algorithms.items():
        times = [measure_time(func, input_list) for _ in range(3)]  # Average over 3 runs
        avg_time = sum(times) / len(times)
        results[alg].append(avg_time)
        print(f"{alg} for size {size}: {avg_time:.6f} seconds")

# Save results to CSV
with open('sorting_results.csv', 'w', newline='') as csvfile:
    fieldnames = ['Input Size'] + list(algorithms.keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i, size in enumerate(sizes):
        row = {'Input Size': size}
        for alg in algorithms:
            row[alg] = results[alg][i]
        writer.writerow(row)

# Plotting the results
for alg in algorithms:
    plt.plot(sizes, results[alg], label=alg)

plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Performance')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.grid(True)
plt.savefig('sorting_performance.png')
plt.show()
