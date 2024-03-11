def find_subsequences(s):
    if len(s) == 0:
        return ['']
    rest_subs = find_subsequences(s[1:])
    return rest_subs + [s[0] + sub for sub in rest_subs]


print(find_subsequences("abc"))  # Output: ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']
