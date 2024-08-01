if __name__ == '__main__':
    N = int(input())
    
    L=[]
    for i in range(N):
        ops=list(input().split())
        index=0
        if len(ops)>1:
            index=ops[1]
        val=ops[-1]
        if ops[0]=='insert':
            L.insert(int(index), int(val))
        elif ops[0]=='remove':
            L.remove(int(val))
        elif ops[0]=='append':
            L.append(int(val))
        elif ops[0]=='sort':
            L.sort()
        elif ops[0]=='pop':
            L.pop()
        elif ops[0]=='reverse':
            L.reverse()
        else:
            print(L)
