class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        def lastchar(word):
            return word[-1]
        s.sort(key=lastchar)

        res=''
        for i in s:
            res+=i[:-1]+' '

        return res[:-1]
