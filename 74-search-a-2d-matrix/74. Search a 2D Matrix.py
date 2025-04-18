class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for sublist in matrix:
            if self.binary_search(sublist, target): return True
        
        return False
    
    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        
        while left <= right: 
            middle = (left + right) // 2
            if arr[middle] == target:
                return True
            elif arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False
        