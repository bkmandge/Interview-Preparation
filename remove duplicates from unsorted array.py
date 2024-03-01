# Brute:- O(n2), O(n)
def removeDuplicates(arr):
    n = len(arr)
    temp = [True] * n
    
    for i in range(n):
        if temp[i]:
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    temp[j] = False
        
    for i in range(n):
        if temp[i]:
            print(arr[i], end=" ")


# Optimal - Hashmap O(n), O(n)
def removeDuplicates2(arr):
    hashMap = {}
    for num in arr:
        if num not in hashMap:
            print(num, end=" ")
            hashMap[num] = 1  # If an element is not present in hashMap, print it and add it to hashMap with count 1.
            

arr = [2,3,1,9,3,1,3,9]  # [2,3,1,9]
arr2 = [4,3,9,2,4,1,10,89,34]  # [3,4,9,2,1,10,34,89]

removeDuplicates2(arr)