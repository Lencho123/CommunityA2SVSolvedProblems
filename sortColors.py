# Two pointer approach
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # move all reds(0) to left
        left,right=0,len(nums)-1
        while left<right:
            while left<right and nums[left]==0:
                left+=1
            if nums[right]==0:
                nums[left],nums[right]=nums[right],nums[left]
            right-=1
        
        # move blue(2) color to right
        left, right=0,len(nums)-1
        while left<right:
            while left<right and nums[right]==2:
                right-=1
            if nums[left]==2:
                nums[right],nums[left]=nums[left],nums[right]
            left+=1
        
        """
        Do not return anything, modify nums in-place instead.
        """ 
# 2-> Counting approach
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count={0:0,1:0,2:0}
        for i in nums:
            count[i]+=1
        
        index=0
        for i in count:
            for j in range(count[i]):
                nums[index]=i
                index+=1
