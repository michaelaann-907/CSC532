import time
import random


#print("\nInsertion-Sort Algorithm")

# Insertion-Sort Algorithm
def insertion_sort(a):
    # Iterate through each element in the array starting from the second element
    for j in range (1, len(a)):
        # current element to be inserted
        key = a[j]

        # move elements greater than key up one position
        i = j - 1
        # loop checks if i is greater than or equal to 0 and key is less than a[i]
        while i >= 0 and key < a[i]:
            # shift elements to the right to make space for key
            a[i + 1] = a[i]
            i = i -1

        # place key at correct position in sorted array
        a[i + 1] = key


# TEST: insertion_sort function using different arrays
"""
a1 = [5, 7, 2, 8, 4, 6]
a2 = [4, 5 , 10, 11, 3, 2]
a3 = [10, 12, 15, 5, 0, 8]

# --array 1--
print("Unsorted Array 1:", a1)
# call function
insertion_sort(a1)
print("Sorted Array 1:", a1)

# --array 2--
print("\nUnsorted Array 2:", a2)
insertion_sort(a2)
print("Sorted Array 2:", a2)
# --array 3--
print("\nUnsorted Array 3:", a3)
insertion_sort(a3)
print("Sorted Array 3:", a3)
"""


#print("\n-----\n\nMerge & Merge-Sort Algorithm")




# Merge Algorithm
def merge(a, p, q, r):
    # calculate the size of the two arrays to be merged
    n1 = q - p + 1
    n2 = r - q

    # create temporary arrays
    left = a[p:p + n1]
    right = a[q + 1: q + 1 + n2]

    # add sentinel values to the end of booth temporary arrays
    left.append(float('inf'))
    right.append(float('inf'))

    i = j = 0

    # merge the two back into original array
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1




# Merge - Sort Algorithm
def merge_sort(a, p, r):
    # recursion "bottoms out" when sequence has length 1
    if p < r:
        # calculate middle index
        q = (p + r) // 2

        # recursive calls to sort the two halves
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)

        # merge the two sorted halves
        merge(a, p, q, r)



# TEST: merge & merge_sort Algorithms
"""
a = [5,7,4,12,15,2,3,1,0,9,14]
print("Before merge-sort: ", a)
# call merge_sort to sort array
merge_sort(a, 0, len(a) - 1)
# print sorted array
print("After merge-sort: ", a)
"""



# Random Array Generator Function
def rand_array(x):
    return [random.randint(0, 100) for _ in range(x)]

# Function to perform sorting experiments
def perform_sorting_experiment(algorithm, array_sizes):
    results = []

    for size in array_sizes:
        array = rand_array(size)

        start_time = time.time()

        if algorithm == insertion_sort:
            sorted_array = array.copy()
            algorithm(sorted_array)
        elif algorithm == merge_sort:
            sorted_array = array.copy()
            algorithm(sorted_array, 0, len(sorted_array) - 1)

        end_time = time.time()

        execution_time = end_time - start_time
        results.append((size, execution_time))

    return results

# Function to print results in a tabular format
def print_results(results, title):
    print(title)
    print("Size\tExecution Time")
    for size, execution_time in results:
        print(f"{size}\t{execution_time:.6f}")


# Function to perform sorting experiments with random arrays
def perform_random_sorting_experiment():
    array_sizes = list(range(100, 10200, 250))
    insertion_results = perform_sorting_experiment(insertion_sort, array_sizes)
    merge_results = perform_sorting_experiment(merge_sort, array_sizes)
    print_results(insertion_results, 'Experiment 1: Sorting Random Arrays')
    print_results(merge_results, 'Experiment 2: Sorting Random Arrays')


# Function to perform sorting experiments with already sorted arrays
def perform_sorted_sorting_experiment():
    array_sizes = list(range(100, 10200, 250))
    insertion_results_sorted = perform_sorting_experiment(insertion_sort, array_sizes)
    merge_results_sorted = perform_sorting_experiment(merge_sort, array_sizes)
    print_results(insertion_results_sorted, 'Experiment 3: Sorting Already Sorted Arrays')
    print_results(merge_results_sorted, 'Experiment 4: Sorting Already Sorted Arrays')


# Main part of the code
perform_random_sorting_experiment()
perform_sorted_sorting_experiment()
