class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length=[]
        for i in strs:
            length.append(len(i))

        mnl=min(length)
        out=''

        for i in range(mnl):
            char=strs[0][i]
            for j in range(len(strs)):
                if strs[j][i]!=char:
                    return out
            out+=char
        return out
