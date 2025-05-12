class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row, target):
            left, right = 0, len(row)-1 
            while left <= right:
                middle = int((left+right)//2)
                if row[middle] == target:
                    return True
                elif row[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return False

        for row in matrix:
            if binary_search(row,target):
                return True
        return False

                


            