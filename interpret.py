class Solution:
    def interpret(self, command: str) -> str:
        res=''
        i=0
        while i <len(command):
            if i< len(command)-1 and (command[i]=='(' and command[i+1]==')'):
                res+='o'
                i+=2
            elif i<len(command)-3 and command[i]=='(':
                res+='al'
                i+=4
            else:
                res+='G'
                i+=1
        return res    
