class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peack=0
        for i in range(len(arr)-2):
            if arr[i]<arr[i+1]>arr[i+2]:
                peack+=1
            elif arr[i]>=arr[i+1]<=arr[i+2]:
                return False
        if peack==1:
            return True
        return False

        
