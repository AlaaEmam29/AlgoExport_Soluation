def isPalindrome(string , i =0):
    #O(N)T    O(1)Space 
    l = 0
    r = len(string) - 1
    while l < r:
        if string[l] != string[r]:
            return False
        l +=1
        r -=1
    return True
