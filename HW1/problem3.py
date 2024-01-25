
# Insertion-Sort Algorithm
def insertionSort(a):
    # Iterate through each element in the array starting from the second element
    for i in range (1, len(a)):
        key = a[i]  # current element compared & inserted
        j = i - 1   # index of previous element

        # increase elements position by one if greater than key
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j = j -1

        # place key at after the element
            a[j + 1] = key


a= [10, 3, 5, 7, 0]
print("Unsorted Array: ", a)
insertionSort(a)
print("Sorted Array: ", a)



