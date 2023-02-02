def generateDocument(characters, document):
    #O(n + m)TS
    hashD = {}
    hashCh = {}
    for c in characters:
        hashCh[c] = hashCh.get(c , 0)  + 1
    for d in document:
        hashD[d] = hashD.get(d , 0) + 1
    for key in hashD:
        if key not in hashCh or hashCh[key] < hashD[key]:
            return False
    return True or len(document) == 0
    
