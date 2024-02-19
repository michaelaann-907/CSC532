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
