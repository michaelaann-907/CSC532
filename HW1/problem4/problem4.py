import random
import time


def maxCrossingSubarrayBook(aList, low, mid, high):
    """
    Introduction to Algorithms 3rd Edition Pseudocode for the max crossing subarray problem.
    :param aList: a list of numbers
    :param low: let half of the array
    :param mid: middle of the array
    :param high: right half of the array
    :return: max crossing subarray
    """
    leftSum = float('-inf')
    summ, maxLeft, maxRight = 0, 0, 0
    for i in range(mid, low - 1, -1):
        summ = summ + aList[i]
        if summ > leftSum:
            leftSum = summ
            maxLeft = i
    rightSum = float('-inf')
    summ = 0
    for j in range(mid + 1, high + 1, 1):
        summ = summ + aList[j]
        if summ > rightSum:
            rightSum = summ
            maxRight = j
    return maxLeft, maxRight, leftSum + rightSum


def maxSubarrayBruteForce(aList):
    """
    This method would use a pair of nested loops where the outer loop iterates through all the possible starting indices
    (0 through the length of the list) and the inner loop iterates through all the possible ending indices
    (the starting index through the length of the list).
    Compute the sum of the values between those two indices [inclusive] and keep track of
    the biggest sum you’ve found so far.
    :param aList: a List of numbers to use.
    :return: the maximum subarray found in aList.
    """
    maxSum = float('-inf')
    lowerIndex, rightIndex = 0, 0
    for i in range(len(aList) - 1):
        subSum = aList[i]
        for j in range(i + 1, len(aList)):
            subSum = subSum + aList[j]
            if subSum > maxSum:
                maxSum = subSum
                lowerIndex = i
                rightIndex = j
    return lowerIndex, rightIndex, maxSum


def main():
    aList = []
    for i in range(10):
        aList.append(random.randint(-10, 20))

    print(aList)
    print(maxSubarrayBruteForce(aList))
    print(maxCrossingSubarrayBook(aList, 0, (len(aList) - 1) // 3, len(aList) - 1))
    print(find_max_subarray_book(aList, 0, len(aList) - 1))

    for i in range(100, 10001, 500):
        list2 = []
        for y in range(i):
            list2.append(random.randint(-1000, 1000))
        startTime = time.perf_counter()
        maxSubarrayBruteForce(list2)
        endTime = time.perf_counter()
        print(i, '\t', endTime - startTime)

        # startTime = time.perf_counter()
        # maxCrossingSubarrayBook(aList, 0, (len(aList) - 1) // 3, len(aList) - 1)
        # endTime = time.perf_counter()
        # print(i, '\t', endTime - startTime)


if __name__ == "__main__":
    main()
