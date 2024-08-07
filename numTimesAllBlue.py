class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxrun=flips[0]
        countOne=0
        res=0

        for i in range(len(flips)):
            maxrun=max(maxrun, flips[i])
            countOne=i+1

            if countOne==maxrun:
                res+=1
        return res
        
