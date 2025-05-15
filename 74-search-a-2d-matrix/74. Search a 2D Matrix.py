class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1
        
        while top <= bottom:
            mid = (top+bottom) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break

        if top > bottom:
            return False
        
        row_index = (top+bottom) // 2
        row = matrix[row_index]
        l, r = 0, cols - 1
        while l <= r:
            mid = (l+r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False