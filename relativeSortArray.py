class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict1={}
        for i in arr1:
            dict1[i]=dict1.get(i, 0)+1

        res=[]

        for i in arr2:
            for j in range(dict1[i]):
                res.append(i)

        other=[]
        for  i in arr1:
            if i not in arr2:
                other.append(i)
        other.sort()
        res=res+other
        
        return res
