class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)       # number of rows
        n = len(matrix[0])    # number of columns

        left  = 0
        right = m * n - 1     # total elements - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n        # which row?
            col = mid % n         # which column?
            val = matrix[row][col]

            if val == target:
                return True
            elif target > val:
                left  = mid + 1   # search right half
            else:
                right = mid - 1   # search left half

        return False