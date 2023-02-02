def groupAnagrams(words):
    #O(26*M*N) ==> O(M*N)T | O(26M) ==> O(M) Space
    hashWords = {}
    for word in words:
        count = [0 for _ in range(26)]
        for char in word:
            count[ord('a') - ord(char)] +=1
        if tuple(count) in hashWords:
            hashWords[tuple(count)].append(word)
        else:
            hashWords[tuple(count)] = [word]
            
    return list(hashWords.values())