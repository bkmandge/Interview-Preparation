'''
                        74. Search a 2D Matrix (Medium)
-> Search given target in m * n matrix. Return True if found else return False
-> Binary Search:-
    1. for searching exact row
    2. for searching exact location of searchValue
'''
from typing import *


class Solution:
    def searchMatrix(self, matrix: List[int], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            curRow = (top + bottom) // 2
            if target > matrix[curRow][-1]:  # current rows last max value matrix[curRow][-1]
                top = curRow + 1   # go to next row & search
            elif target < matrix[curRow][0]:  # current rows first smallest value matrix[curRow][0]
                bottom = curRow - 1  # go to previous row & search
            else:
                break  # found in current row

        # if value does not exist in neither of rows or columns, return False else continue binary search
        if not (top <= bottom):
            return False
        curRow = (top + bottom) // 2
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[curRow][mid]:
                l = mid + 1
            elif target < matrix[curRow][mid]:
                r = mid - 1
            else:
                return True
        return False


result = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3

print(result.searchMatrix(matrix, target))
