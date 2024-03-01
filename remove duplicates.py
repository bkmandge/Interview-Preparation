# Brute Force Approach: O(N) + O(K) + O(K) = O(N + K), SC - O(N)
def removeDuplicates(arr):
    n = len(arr)
    st = set()
    
    for i in range(n):  # O(N)
        st.add(arr[i])
    
    k = len(st)  # add and count unique elements & put them back in array
    i = 0  # starting index for arr
    
    for num in st:      # O(K)
        arr[i] = num
        i += 1
    print(k)

    # print array unique elements
    for i in range(k):      # O(K)
        print(arr[i])


# Optimal Approach -> Two pointers
def removeDuplicates2(arr):
    n = len(arr)
    i = 0
    count = 0
    
    for j in range(1, n):
        if arr[i] == arr[j]:  # if same element cotinue to next element
            continue
        else:
            i += 1
            arr[i] = arr[j]
            count += 1
            
    return count + 1
    

arr = [1, 1, 2, 2, 2, 3, 3]
print(removeDuplicates2(arr))
