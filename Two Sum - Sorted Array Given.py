# Check if given target sum is present by adding two digits
# Binary search works only if given array is sorted
# In unsorted array use Hashmap to find two sum

def two_sum(lst, target):
    start = 0
    end = len(lst) - 1
    while start < end:
        if lst[start] + lst[end] == target:
            return f"Found sum at index {start} and {end}"
        elif lst[start] + lst[end] > target:
            end = end - 1
        else:
            start = start + 1
    return "Not found!"


lst = [5, 7, 11, 22, 30]
target = 18
print(two_sum(lst, target))

