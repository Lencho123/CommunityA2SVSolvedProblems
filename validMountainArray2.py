class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        numberOfpeaks=0
        for i in range(1,len(arr)-1):
            # count nu of peack
            if arr[i-1]<arr[i]>arr[i+1]:
                numberOfpeaks+=1
                # check if there is plateou and valley
            if arr[i]==arr[i-1] or arr[i]==arr[i+1] or arr[i-1]>arr[i]<arr[i+1]:
                return False

        return numberOfpeaks==1
