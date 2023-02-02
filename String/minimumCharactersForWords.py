def minimumCharactersForWords(words):
    #O(n * L * (n + L)) T | O(C)
    listOfWords = []
    for w in words:
        for c in w:
            if c in listOfWords:
                if w.count(c) > listOfWords.count(c):                    
                    for i in range(w.count(c) - listOfWords.count(c)):
                        listOfWords.append(c)
                else:
                    continue
            else:
                listOfWords.append(c) 

    return listOfWords
                
                
            
def minimumCharactersForWords(words):
    # O(N * I)Time I longest word , N -> number of words
    #O(C)number of unique characters
    maxFrequencies = {}
    for word in words:
        wordFreq = countCharFreq(word)
        unpateMaxFrequencies(wordFreq , maxFrequencies)
    return makeList(maxFrequencies)
        
def countCharFreq(word):
    wordFreq = {}
    for char in word:
        wordFreq[char] = wordFreq.get(char , 0) + 1
    return wordFreq
def unpateMaxFrequencies(word , maxDict):
    for char in word:
        count = word[char]
        if char in maxDict:
            maxDict[char] = max(count  , maxDict[char])
        else:
            maxDict[char] = count
    return maxDict

def makeList(dictList):
    res = []
    for key,count in dictList.items():
        for _ in range(count):
            res.append(key)
    return res
        
        
        