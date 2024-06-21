class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        for i in range(r):
            for j in range(c):
                if i>0 and j>0:
                    if matrix[i][j]!=matrix[i-1][j-1]:
                        return False
        return True
        
