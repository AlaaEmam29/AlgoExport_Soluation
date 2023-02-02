def moveElementToEnd(array, toMove):
    #O(N) Time | O(n+K) Space
    moveArray = []
    arr = []
    for i in range(len(array)):
        if array[i] == toMove:
            moveArray.append(array[i])
        else:
            arr.append(array[i])
    return arr + moveArray
def moveElementToEnd(array, toMove):
    #O(NlogN) Time | O(1) Space 
    array.sort()
    l = 0
    r = len(array )- 1
    while l < r:
        if array[l] < toMove:
            l +=1
        else:
            array[l] , array[r] = array[r] , array[l]
            l += 1
            r -= 1
    return array
def moveElementToEnd(array, toMove):

    # O(N) Time | O(1)Space
    temp = 0
    for i in range(len(array)):
        if array[i] != toMove:
            array[i] , array[temp]=  array[temp] ,  array[i] 
            temp += 1
    return array
        
