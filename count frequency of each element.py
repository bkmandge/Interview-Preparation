# Brute Force Approach:- TC O(N2), SC O(N)
def countFrequency(arr):
    n = len(arr)
    visited = [False] * n
    
    for i in range(n):
        if visited[i] is True:
            continue
        count = 1
        
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
        
        print(arr[i], count)
        

# Hashmap:- TC O(N), O(N)
def countFrequency3(arr, char):
    n = len(arr)
    hashMap = {}  
        
    for i in range(n):
        if arr[i] in hashMap:
            hashMap[arr[i]] += 1  # increase count
        else:
            hashMap[arr[i]] = 1  # add element with count 1

    for char in hashMap:
        print(char, hashMap[char])  # print key - value / count pairs
    
    
arr = [10, 5, 10, 15, 10, 5]
print(arr)
print(countFrequency2(arr, 10))
        