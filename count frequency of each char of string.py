# brute force
def countFreq(s):
    for ch in s:
        freq = s.count(ch)
        print(f"{ch} : {str(freq)}")

# use built-in hashmap
from collections import Counter

def countFreq2(s):
    freq = Counter(s)
    return freq


s = "youkeepcoding"
print(countFreq2(s))

        