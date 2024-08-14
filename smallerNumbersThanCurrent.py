class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortednum=sorted(nums)
        count=defaultdict(int)
        for i in range(len(sortednum)):
            if not sortednum[i] in count:
                count[sortednum[i]]=i
        
        res=[]
        for i in nums:
            res.append(count[i])
        return res
