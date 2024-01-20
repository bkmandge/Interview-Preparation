"""
                        Shuffle The Array

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2, 3, 5, 4, 1, 7]

Trick:- Use bit manipulation

"""


def shuffleArray(nums, n):
    for i in range(n):
        nums[i] = nums[i] << 10
        nums[i] = nums[i] | nums[i + n]  # stores x, y

    j = 2 * n - 1  # nums length 2n given in constraint
    for i in range(n-1, -1, -1):  # iterate first half of array in reverse order from middle of array
        y = nums[i] & (2 ** 10 - 1)
        x = nums[i] >> 10
        nums[j] = y
        nums[j - 1] = x
        j -= 2

    return nums


nums = [2,5,1,3,4,7]
n = 3
print(shuffleArray(nums, n))

