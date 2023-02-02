def sortedSquaredArray(array):
    # O(N) Time | O(N) Space
    smallest = 0
    largest = len(array) - 1
    sortedSquare = [0 for _ in array]
    for i in reversed(range(len(array))):
        if abs(array[smallest]) > abs(array[largest]):
            sortedSquare[i] = array[smallest] * array[smallest]
            smallest += 1
        else:
            sortedSquare[i] = array[largest] * array[largest]
            largest -= 1
    return sortedSquare
def sortedSquaredArray(array):
    #O(nlogn) merge| sort (Time) || O(n) space
    res = [0 for _ in array]
    for i in range(len(array)):
        res[i] = array[i] * array[i]
    res.sort()
    return res

    
            


