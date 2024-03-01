nums = [2,5,1,3,0]
n = len(nums)

mini = float("inf")
for i in range(n):
    if mini > nums[i]:
        mini = nums[i]
print(mini)


