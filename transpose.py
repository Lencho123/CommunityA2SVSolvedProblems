class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose=[[0 for _ in range(len(matrix))] for j in range(len(matrix[0]))]
        print (transpose)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transpose[j][i]=matrix[i][j]
        return transpose
