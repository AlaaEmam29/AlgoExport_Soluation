def kadanesAlgorithm(array):
    #O(N)Time ||O(1)Space
    currentNum = 0
    maxNum = float("-inf")
    for num in array:
        currentNum = max(currentNum , 0) + num
        maxNum = max(maxNum , currentNum)
    return maxNum
