"""                     Calculate Frequency of characters in a String
s = articles -> a1 c1 e1 i1 l1 r1 s1 t1 


"""
def countFrequency(s):
    freq = [0] * 26
    # creating hashArray
    for char in s:
        if char.isalpha():
            idx = ord(char.lower()) - ord("a")
            freq[idx] += 1
    
    # printing counts from hashArray
    for i in range(26):
        if freq[i] != 0:
            print(chr(i + ord('a')) + str(freq[i]), end=" ")
            # chr(i + ord('a')) - > keys -> a, c, e, i, r ... 
            # str(freq[i]) -> values / counts -> 1, 1, 1...
               
s = "articles"
countFrequency(s)