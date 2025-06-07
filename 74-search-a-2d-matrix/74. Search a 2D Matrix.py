class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        row = -1

        while top <= bottom: 
            mid = (top+bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                bottom = mid - 1
        
        if row == -1: 
            return False
        
        l, r = 0, len(matrix[row])-1
        while l <= r: 
            mid = (l+r)//2
            if matrix[row][mid] == target: 
                return True
            elif matrix[row][mid] < target: 
                l = mid + 1
            else:
                r = mid - 1
        
        return False