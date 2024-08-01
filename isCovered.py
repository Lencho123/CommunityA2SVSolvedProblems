class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        pre=[0]*51
        for i in ranges:
            pre[i[0]-1]+=1
            pre[i[1]]-=1
        
        for i in range(1, 51):
            pre[i]=pre[i]+pre[i-1]
    
        for i in range(left-1, right, 1):
            if pre[i]<1:
                return False
        
        return True
