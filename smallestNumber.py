class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>=0:
            num=str(num)
            num=list(num)
            zeros=0
            for i in num:
                if i == '0':
                    zeros+=1
            num.sort()
            num=''.join(num)
            num=str(int(num))

            if len(num)>1:
                num=num[0]+'0'*zeros+num[1:]
            else:
                num=num+'0'*zeros

            return int(num)
        
        else:
            num=str(num)
            num=num[1:]
            num=list(num)
            num.sort(reverse=True)

            num='-'+''.join(num)

            return int(num)
        
