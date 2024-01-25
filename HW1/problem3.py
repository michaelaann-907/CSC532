
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






# Merge Algorithm





# Merge - Sort Algorithm








