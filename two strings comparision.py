def string_comparison(s1, s2):
    if s1 == s2:
        return 0
    elif s1 < s2:
        return -1
    else:
        return 1

# Test
print(string_comparison("apple", "banana"))  # Output: -1
