class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res=[]
        for r in range(len(grid)-2):
            rval=[]
            for c in range(len(grid)-2):
                cval=max(grid[r][c], grid[r][c+1], grid[r][c+2],grid[r+1][c], grid[r+2][c], grid[r+1][c+1], grid[r+2][c+2], grid[r+2][c+1], grid[r+1][c+2])
                rval.append(cval)
            res.append(rval)
        return res

        
