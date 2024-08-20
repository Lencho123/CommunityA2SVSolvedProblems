class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        counter=Counter(nums)

        checked=set()
        minval=min(nums)
        pre=0
        res=0
        for i in nums:
            if i not in checked and i != minval:
                pre+=counter[i]
                res+=pre
                checked.add(i)

        return res
