class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        sample=Counter(words[0])
        for i in words:
            cur_sample=Counter(i)
            for j in sample:
                sample[j]=min(sample[j], cur_sample[j])
        
        out=[]
        for i in sample:
            for j in range(sample[i]):
                out.append(i)
        
        return out
