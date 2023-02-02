def twoNumberSum(array, targetSum):
    # o(n) Time , O(n) Space
    hashMap = {}
    for idx , value in enumerate(array):
        diff = targetSum - value
        if diff in hashMap:
            return[value , diff]
        hashMap[value] = idx
    return[]
    
