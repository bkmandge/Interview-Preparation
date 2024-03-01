# Brute Force Approach T.C. O(N), S.C. O(N) - creating extra array to store result
def reverseElements(arr):
    n = len(arr)
    ans = [0] * n
    
    # we are doing arr reverse traversal)
    for i in range(n - 1, -1, -1):
        # ans[n - i - 1] -> (1st iteration ) -> 5 - 4 - 1 = at 0 index -> places last element
        ans[n - i - 1] = arr[i]  
    return ans


# Two pointers - Iterative
def reverseElements2(arr):
    n = len(arr)
    left = 0
    right = n - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
    

# Two pointers - Recursive - need to give start and end indices
def reverseElements3(arr, start, end):   
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        reverseElements3(arr, start + 1, end - 1)
    return arr

    
arr = [5, 4, 3, 2, 1]
n = len(arr)

print(reverseElements3(arr, 0, n - 1))