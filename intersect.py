class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1=Counter(nums1)
        counter2=Counter(nums2)

        res=[]
        for i in counter1:
            if i in counter2:
                res+=[i]*min(counter1[i], counter2[i])
        return res
