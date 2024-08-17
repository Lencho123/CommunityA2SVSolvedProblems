class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        nums.sort(reverse=True)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                asc=nums[i]+nums[j]
                dsc=nums[j]+nums[i]
                if dsc>asc:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp

        res=str(int(''.join(nums)))
        return res
            
        
