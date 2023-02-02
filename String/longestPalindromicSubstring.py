def longestPalindromicSubstring(string):
    # O(N^2) Time  |O(N)S
    longestSub = [0,1]
    for i in range(1 , len(string)):
        leftIdx , currIdx , rightIdx = i-1 , i , i+1
        odd = getLengthFromPalindrom(string , leftIdx, rightIdx)
        even = getLengthFromPalindrom(string , leftIdx, currIdx)
        length = max(odd , even , key = lambda x:x[1] - x[0])
        longestSub = max(length , longestSub , key = lambda x:x[1] - x[0])
    return string[longestSub[0] : longestSub[1]]

def getLengthFromPalindrom(string , leftIdx , rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -=1
        rightIdx +=1
    return [leftIdx + 1 , rightIdx]