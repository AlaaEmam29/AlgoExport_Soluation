from collections import defaultdict
def firstNonRepeatingCharacter(s):
    #O(N)T ===> O(1) only need 26 key cuz we store alphabet
    charCounts = {} 
    for char in s:
        charCounts[char] = charCounts.get(char, 0) + 1
    for i in range(len(s)):
        if charCounts[s[i]] == 1:
            return i
    return -1