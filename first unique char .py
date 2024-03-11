def first_unique_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    print(char_count)
    
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    return -1

# Test
print(first_unique_char("leetcode"))  # Output: 0
