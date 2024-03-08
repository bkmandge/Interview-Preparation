def lengthOfLastWord(s):
    n = len(s)
    i = n - 1       # index of last char
    length = 0

    # deleting space from last
    while s[i] == " ":
        i = i - 1

    while i >= 0 and s[i] != " ":
        length = length + 1
        i = i - 1

    return length


s = "Hello World"       # 5
s2 = "   fly me   to   the moon  "      # 4

print(lengthOfLastWord(s))
print(lengthOfLastWord(s2))

