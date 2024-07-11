class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(arr, target):
            l=0
            r=len(arr)-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]==target:
                    return True
                elif arr[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return False

            
        for i in matrix:
            boolval=binarySearch(i,target)
            if boolval:
                return True
        return False
