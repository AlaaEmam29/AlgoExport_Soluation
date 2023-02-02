def smallestSubstringContaining(bigString, smallString):
    res = []
    hashSmallWord = {}
    for i in smallString:
        hashSmallWord[i] = hashSmallWord.get(i, 0) + 1
    for i in range(len(bigString)):
        for j in range(len(bigString)):
            subString = bigString[i :j+1]
            if all(x in subString for x in smallString) and len(set(subString)) > len(set(smallString)):
                res.append(subString)
    smallest = []
    for word in res:
        if all(word.count(x) >= hashSmallWord[x] for x in smallString):
            smallest.append(word)
    return min(smallest, key=len)