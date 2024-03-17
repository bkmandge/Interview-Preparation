# Return any permutation of s
def customSortString(order: str, s: str) -> str:
    # creating hashmap with count 0
    # count = {char: 0 for char in order}
    count = {}
    for ch in order:
        count[ch] = 0
    # print(count)
    
    # add count of same char from both strings s and order in count hashmap
    for ch in s:
        if ch in count:
            count[ch] += 1
    
    print(count)
    
    # Build the result string based on the custom order
    result = ""
    for ch in order:
        result = result + ch * count[ch]
    print(result)    
    
    # Add the remaining characters in s that are not in order
    for ch in s:
        if ch not in order:
            result = result + ch
    
    return result
    

# order = "cba"
# s = "abcd"     

order = "bcafg"; s = "abcd"

print(customSortString(order, s))
