class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # transpose
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix [i][j]
        
        # reverse
        for i in range(len(matrix)):
            start = 0 
            end = len(matrix[i]) - 1
            while(start < end):
                matrix[i][end], matrix[i][start] = matrix[i][start], matrix[i][end]
                start+=1
                end-=1
        