"""                 Find maximum and minimum number in a subarray of size k.

"""
# Brute Force:- O((n - k + 1) * k)
def minAndMaxInSubArrray(arr, k):
    n = len(arr)
    if not arr or k < 0 or k > n:
        return []
    print(arr)
    max_min_pairs = []
    for i in range(n - k + 1):
        subarray = arr[i : i + k]  # subarray generation
        maxii = max(subarray)
        minii = min(subarray)
        max_min_pairs.append((maxii, minii))
        
        print(subarray)
    return max_min_pairs


# Optimal Approach
from collections import deque

def minAndMaxInSubArrray2(arr, k):
    n = len(arr)
    if not arr or k <= 0 or k > n:
        return []
    
    max_min_pairs = []
    maxQ = deque()
    minQ = deque()
    
    def popQueue(queue, idx):
        if queue and queue[0] == idx:
            queue.popleft()
            
    # Remove elements outside the window from the queue
    for i in range(n):
        popQueue(maxQ, i - k)
        popQueue(minQ, i - k)
    
        # Remove elements from the queue which are less than current element
        while maxQ and arr[i] >= arr[maxQ[-1]]:   # corrected comparison, use arr[i] >= arr[maxQ[-1]]
            maxQ.pop()
        
        while minQ and arr[i] <= arr[minQ[-1]]:   # corrected comparison, use arr[i] <= arr[minQ[-1]]
            minQ.pop()

        # Add current element's index to the queue  
        maxQ.append(i)
        minQ.append(i)
        
        # Append max/min element of the current window to the result
        if i >= k - 1:
            max_min_pairs.append((arr[maxQ[0]], arr[minQ[0]]))
        
    return max_min_pairs


arr = [10, 5, 2, 7, 8, 7]
k = 3

print(minAndMaxInSubArrray2(arr, k))

