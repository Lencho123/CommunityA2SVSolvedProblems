class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        runsum,count=0,0
        for i in costs:
            runsum+=i
            if runsum<=coins:
                count+=1
        return count
