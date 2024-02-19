"""
The problem with Quicksort is that its worst-case behavior can occur if the list is sorted
(or almost sorted).Test all 3 algorithms (Heap, Merge, Quick) when sorting already sorted
arrays. How large an array can you do before Quicksort completely bombs?

The book’s solution is to randomly select the pivot in the partitioning step.
(See Section 7.3).  Implement that change to the algorithm and run experiments
(with accompanying graphs) to show that it actually works.
"""

import random  # Importing the random module for generating random numbers
import timeit  # Importing the timeit module for measuring execution time

# Function to partition the array for Quicksort
def partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Randomly select a pivot index
    pivot = arr[pivot_index]  # Select the pivot element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot element to the end
    i = low - 1  # Initialize the index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap arr[i] and arr[j]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Move pivot to its correct position
    return i + 1  # Return the index of the pivot element after partitioning


# Quicksort function to sort the array
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # Get the partitioning index
        quicksort(arr, low, pi - 1)  # Recursively sort elements before partition
        quicksort(arr, pi + 1, high)  # Recursively sort elements after partition


# Function to merge two subarrays for Mergesort
def merge(arr, l, m, r):
    n1 = m - l + 1  # Length of left subarray
    n2 = r - m  # Length of right subarray

    L = [0] * n1  # Create temporary arrays for left and right subarrays
    R = [0] * n2

    # Copy data to temporary arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    # Merge the temporary arrays back into arr[l..r]
    i = j = 0  # Initial indexes of left and right subarrays
    k = l  # Initial index of merged subarray
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# Mergesort function to sort the array
def mergesort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2  # Calculate the middle index

        # Recursively sort the two halves
        mergesort(arr, l, m)
        mergesort(arr, m + 1, r)
        # Merge the sorted halves
        merge(arr, l, m, r)


# Heapsort function to sort the array
def heapsort(arr):
    # Heapify the array
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1  # Left child index
        r = 2 * i + 2  # Right child index

        # If left child exists and is larger than root
        if l < n and arr[i] < arr[l]:
            largest = l

        # If right child exists and is larger than largest so far
        if r < n and arr[largest] < arr[r]:
            largest = r

        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap
            heapify(arr, n, largest)  # Heapify the affected sub-tree

    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)


# Function to test sorting algorithms
def test_sorting_algorithm(algorithm, array_sizes):
    results = []  # Store results
    for size in array_sizes:
        arr = list(range(size))  # Create an array of specified size
        random.shuffle(arr)  # Randomize array
        start_time = timeit.default_timer()  # Start time measurement
        if algorithm == heapsort:
            algorithm(arr)  # Pass only the array to heapsort
        else:
            algorithm(arr, 0, len(arr) - 1)  # Pass array, low, and high to other sorting algorithms
        end_time = timeit.default_timer()  # End time measurement
        time_taken = end_time - start_time  # Calculate time taken
        results.append((size, time_taken))  # Store size and time taken
    return results  # Return results



### Experiments Done ###
# To run each one, you will have to comment out the other ones
# while running one since they all share the same variable name.



## General Experiment (Wid Range of Sizes)
array_sizes = [10, 100, 1000, 10000, 100000]  # Specify array sizes for testing

## Experiment 1 (Small Array Sizes)
#array_sizes = [10, 50, 100, 200, 500]  # Small array sizes

## Experiment 2 (Medium Array Sizes)
#array_sizes = [100, 500, 1000, 5000, 10000]  # Medium array sizes

## Experiment 3
#array_sizes = [5000, 10000, 20000, 50000, 100000]  # Large array sizes




# Test the algorithms
quicksort_results = test_sorting_algorithm(quicksort, array_sizes)  # Test Quicksort
mergesort_results = test_sorting_algorithm(mergesort, array_sizes)  # Test Mergesort
heapsort_results = test_sorting_algorithm(heapsort, array_sizes)  # Test Heapsort

# Print results in tabular format
print("Array Size\tQuicksort (Random Pivot)\tMergesort\tHeapsort")
for i in range(len(array_sizes)):
    size = array_sizes[i]
    quicksort_time = quicksort_results[i][1]
    mergesort_time = mergesort_results[i][1]
    heapsort_time = heapsort_results[i][1]
    print(f"{size}\t{quicksort_time}\t{mergesort_time}\t{heapsort_time}")  # Print results


"""
Testing large array values to see when QuickSort "bombs"

def test_quicksort_performance(max_array_size):
    array_size = 100
    while array_size <= max_array_size:
        arr = list(range(array_size))
        random.shuffle(arr)
        start_time = timeit.default_timer()
        quicksort(arr, 0, len(arr) - 1)
        end_time = timeit.default_timer()
        time_taken = end_time - start_time
        print(f"Array size: {array_size}, Time taken: {time_taken} seconds")
        array_size *= 2

# Test Quicksort performance
max_array_size = 10**9  # Adjust as needed
test_quicksort_performance(max_array_size)
"""