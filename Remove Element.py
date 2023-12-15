
def remove_element(nums, val):
    if not nums:
        return 0

    k = 0  # counter var to keep track of length of array

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


nums = [3, 2, 2, 3, 4, 5, 6, 3]
val = 3
print(f"Original array: {nums}")
result = remove_element(nums, val)


# slice of the nums list, including elements from the beginning (index 0) up to, but not including, the index result
print(f"Modified array is: {nums[:result]}")
print(nums[:result])
print(f"Number of elements not equal to {val} is: {result}")
