class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        end,index,k=len(piles)//3,1,1
        res=0
        while k<=end:
            res+=piles[index]
            k+=1
            index+=2
        return res
        
