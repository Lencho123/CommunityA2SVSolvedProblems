from collections import defaultdict

t=int(input())

for _ in range(t):
    n,m = map(int, input().split())
    grid=[]
    for i in range(n):
        row=list(map(int, input().split()))
        grid.append(row)
        
    leftToRight=defaultdict(int)
    rightToLeft=defaultdict(int)

    mxval=0
    for r in range(n):
        for c in range(m):
            leftToRight[r-c]+=grid[r][c]
            rightToLeft[r+c+2]+=grid[r][c]

    for i in range(n):
        for j in range(m):
            mxval=max(leftToRight[i-j]+rightToLeft[i+j+2]-grid[i][j],mxval)
    print(mxval)
