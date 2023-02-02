def nonConstructibleChange(coins):
    #O(MlogN) T || O(1)S 
    coins.sort()
    smallChange = 0
    for idx , value in enumerate(coins):
        if value > smallChange + 1:
            return smallChange + 1
        smallChange += value
    return smallChange + 1