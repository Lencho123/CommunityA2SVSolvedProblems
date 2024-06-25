class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l=len(arr)
        res=[-1]*l
        mxval=arr[-1]

        for i in range(l-2, -1,-1):
            res[i]=mxval
            mxval=max(mxval, arr[i])
            
        return res
