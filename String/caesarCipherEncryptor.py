def caesarCipherEncryptor(string, key):
    # O(N)TS
    newS = []
    key = key % 26
    for s in string:
        int_ascii = ord(s) + key 
        if int_ascii > ord("z"):
            int_ascii -=26
        newS.append(chr(int_ascii))
    return "".join(newS)

