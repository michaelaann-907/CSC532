

print("\nInsertion-Sort Algorithm")

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

# Testing insertion_sort function using different arrays
a1 = [5, 7, 2, 8, 4, 6]
a2 = [4, 5 , 10, 11, 3, 2]
a3 = [10, 12, 15, 5, 0, 8]

# array 1
print("Unsorted Array 1:", a1)
# call function
insertion_sort(a1)
print("Sorted Array 1:", a1)

# array 2
print("\nUnsorted Array 2:", a2)
insertion_sort(a2)
print("Sorted Array 2:", a2)

# array 3
print("\nUnsorted Array 3:", a3)
insertion_sort(a3)
print("Sorted Array 3:", a3)



print("\n-----\n\nMerge & Merge-Sort Algorithm")

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


# Testing merge & merge_sort Algorithms
a = [5,7,4,12,15,2,3,1,0,9,14]
print("Before merge-sort: ", a)
# call merge_sort to sort array
merge_sort(a, 0, len(a) - 1)
# print sorted array
print("After merge-sort: ", a)






