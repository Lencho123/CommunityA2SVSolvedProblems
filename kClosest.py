class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceWithIndex=[]
        for i in range(len(points)):
            distanceWithIndex.append([(points[i][0]**2 + points[i][1]**2)**0.5, i])
        
        distanceWithIndex.sort()
        res=[]
        for i in range(k):
            res.append(points[distanceWithIndex[i][1]])
        
        return res
