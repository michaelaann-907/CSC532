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

