def isValidSubsequence(array, sequence):
    #O(N) Time | O(1) Space
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)
        
        
