class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zippedl=list(zip(heights, names))
        zippedl.sort(reverse=True)

        res=[]
        for i in zippedl:
            res.append(i[1])

        return res
