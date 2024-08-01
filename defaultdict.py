# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m= map(int, input().split())
A=defaultdict(list)
for i in range(n):
    A[input()].append(str(i+1))
    
listB=[]
for j in range(m):
    listB.append(input())
    
for i in listB:
    if i in A:
        print(' '.join(A[i]))
    else:
        print(-1)
