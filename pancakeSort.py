class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # swap function
        def swap(array,right):
            l,r=0,right

            while l<r:
                array[r],array[l]=array[l],array[r]
                l+=1
                r-=1
        
        # Pancake sort
        res=[]
        right=len(arr)
        while right>0:
            index=0
            maxval=arr[0]
            for i in range(right):
                if maxval<arr[i]:
                    maxval=arr[i]
                    index=i

            swap(arr,index)
            res.append(index+1)
            swap(arr,right-1)
            res.append(right)
            right-=1

        return res
