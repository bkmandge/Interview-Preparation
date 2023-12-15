# Check if given target is present or not. If yes return their indices.

def two_sum(arr, target):
    dict1 = {}
    for i, v in enumerate(arr):
        diff_value = target - v
        if diff_value in dict1:
            return f"Indices are at {dict1[diff_value], i}"
        else:
            dict1[v] = i
    return "No such sum!"


arr1 = [3, 2, 8]
target = 11
print(two_sum(arr1, target))
