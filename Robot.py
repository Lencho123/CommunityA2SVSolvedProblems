class Robot:

    def __init__(self, width: int, height: int):
        self.dir=["East","North","West","South"]
        self.width=width-1
        self.height=height-1
        self.dirInd=0
        self.x=0
        self.y=0
        self.perimeter=(width+height)*2-4
        

    def step(self, num: int) -> None:
        num=num%self.perimeter
        if num==0 and [self.x,self.y]==[0,0]:
            self.dirInd=3
        for i in range(num):
            if self.x==self.width and self.dir[self.dirInd]=="East":
                self.y+=1
                self.dirInd=(self.dirInd+1)%4
            elif self.y==self.height and self.dir[self.dirInd]=="North":
                self.x-=1
                self.dirInd=(self.dirInd+1)%4
            elif self.x==0 and self.dir[self.dirInd]=="West":
                self.y-=1
                self.dirInd=(self.dirInd+1)%4
            elif self.y==0 and self.dir[self.dirInd]=="South":
                self.x+=1
                self.dirInd=(self.dirInd+1)%4
            elif self.dir[self.dirInd]=="East":
                self.x+=1
            elif self.dir[self.dirInd]=="West":
                self.x-=1
            elif self.dir[self.dirInd]=="North":
                self.y+=1
            else:
                self.y-=1
            

    def getPos(self) -> List[int]:
        return([self.x, self.y])

    def getDir(self) -> str:
        return(self.dir[self.dirInd])


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
