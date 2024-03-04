def generateSubarrays(s):
    n = len(s)
    subArray = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            subArray.append(s[i:j])
    return subArray


# another way
def generateSubarrays2(s):
    subarrays = []
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            subarray = '[' + s[i:j] + ']'
            subarrays.append(subarray)
    return '\n'.join(subarrays)


s = "code"
print(generateSubarrays2(s))
