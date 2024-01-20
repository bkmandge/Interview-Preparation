'''
                    Square Root of Integer (Easy)
-> Return square root of given number w/o using built-in functions
-> Binary Search
Time: O(logN)

'''

class Solution:
    def floorSqrt(self, x):
        start = 1
        end = x//2
        pos = 1
        while start <= end:
            mid = (start+end) >> 1
            if mid * mid < x:
                pos = mid
                start = mid+1
            elif mid*mid > x:
                end = mid-1
            else:
                return mid
        else:
            return pos


result = Solution()
print(result.floorSqrt(5))


class Solution:
    def floorSqrt(self, x):
        low = 0
        high = x

        while low <= high:
            mid = low + (high - low) // 2
            if mid * mid > x:
                high = mid - 1
            elif mid * mid <= x:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                else:
                    low = mid + 1


result = Solution()
print(result.floorSqrt(2))