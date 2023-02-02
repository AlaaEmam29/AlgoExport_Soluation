def runLengthEncoding(s):
    # O(N)TS
    i = 0
    res = []
    count = 1
    n = len(s) 
    while i < n:
        j = i + 1
        while j < n and s[i] == s[j] and count < 9:
            count +=1
            j+=1
        res.append(str(count))
        res.append(s[i])
        i = j
        count = 1
    return ''.join(res)