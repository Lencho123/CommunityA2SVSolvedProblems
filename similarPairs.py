class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hash={}
        count=0
        for i in words:
            word=set(i)
            word=list(word)
            word.sort()
            word=''.join(word)
            hash[word]=hash.get(word,0)+1
        for i in hash:
            count+=((hash[i]*(hash[i]+1))-2*hash[i])//2
            
        return count
            
        
