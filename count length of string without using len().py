def countLength(s):
    count = 0
    for ch in s:
        count = count + 1
    return count


s = "keepcoding"
print(countLength(s))

# built-in method:- len()
# print(len(s))
