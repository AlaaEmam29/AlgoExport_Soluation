#O(M*N) ===> O(M(each word) N(langest length of word in words))T
def semordnilap(words):
    # Write your code here
    pairs =[] 
    wordSet = set(words)
    for word in words:
        reverseWord = word[::-1] 
        if reverseWord in wordSet and word != reverseWord:
            pairs.append([word, reverseWord])
            wordSet.remove(word)
            wordSet.remove(reverseWord)
    return pairs

        
