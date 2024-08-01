# Enter your code here. Read input from STDIN. Print output to STDOUT
e=int(input())
en=set(map(int, input().split()))
f=int(input())
fr=set(map(int, input().split()))

diff = en.difference(fr)
print(len(diff))
