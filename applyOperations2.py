class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0

        l=0
        print(nums)
        for r in range(1,len(nums)):
            # check for left val to move
            if nums[l]==0:
                # check right val to swap
                if nums[r]!=0:
                    nums[l]=nums[r]
                    nums[r]=0
                    l+=1
            else:
                l+=1

        return nums
            
