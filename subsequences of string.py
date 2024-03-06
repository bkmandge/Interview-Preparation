# Python program to print all subsequence of a given string.

# set to store all the subsequences
st = set()

def subsequence(str):
    n = len(str)
    for i in range(n):
        for j in range(n, i, -1):
            subString = str[i: i+j]
            st.add(subString)

# Drop kth character in the substring and if its not in the set then recur
            for k in range(1,len(subString)):
                sb = subString
                # Drop character from the string
                sb = sb.replace(sb[k],"")
                subsequence(sb)


s = "aabc"
subsequence(s)
for i in st:
    print(i, end=" ")
print()

