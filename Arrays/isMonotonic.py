def isMonotonic(array):
    #O(N) Time | O(1)Space
    isNonDecrease = True
    isNonIncrease = True
    for i in range(1,len(array)):
        if array[i] < array[i - 1]:
            isNonDecrease = False
        if array[i] > array[i - 1]:
            isNonIncrease = False
    return isNonIncrease or isNonDecrease
            
            
