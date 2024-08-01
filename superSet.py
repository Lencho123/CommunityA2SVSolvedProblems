# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(map(int, input().split()))
n=int(input())

b=True
for i in range(n):
    subset=set(map(int, input().split()))
    
    diff=subset.difference(A)
    if diff or subset==A:
        print(False)
        b=False
        break
if b:
    print(True)
