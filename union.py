# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
e=int(input())
en=set(map(int, input().split()))
f=int(input())
fr=list(map(int, input().split()))

diff = en.union(fr)
print(len(diff))
