class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False

        top, bottom = 0, len(matrix)

        def find_target(row):
            left, right = 0, len(matrix[0])
            while left < right:
                mid = left + (right - left) // 2
                if matrix[row][mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return True if left < len(matrix[0]) and matrix[row][left] == target else False


        while top < bottom:
            mid_row = top + (bottom - top) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                # row found
                return find_target(mid_row)
            elif matrix[mid_row][0] > target:
                bottom = mid_row
            else:
                top = mid_row + 1
        return False
