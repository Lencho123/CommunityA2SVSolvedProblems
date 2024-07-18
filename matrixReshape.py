class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res=[]
        row=[]
        colm=0
        l=len(mat)*len(mat[0])
        if l!=r*c:
            return mat
        for i in mat:
            for j in range(len(i)):
                row.append(i[j])
                colm+=1
                if colm==c:
                    res.append(row)
                    row=[]
                    colm=0
        return res
