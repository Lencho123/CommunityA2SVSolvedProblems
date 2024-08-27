class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)

        l=len(tasks)
        tIndex=0
        pIndex=0
        maxTime=0
        while tIndex < l:
            maxTime=max(maxTime, processorTime[pIndex]+tasks[tIndex])
            tIndex+=4
            pIndex+=1
            
        return maxTime
