# brute force
def nonRepeatingChar(s):
    for i in s:
        freq = s.count(i)
                
        if freq == 1:
            print(str(i))


# using hashmap

s = "keepcoding"    
nonRepeatingChar(s)
