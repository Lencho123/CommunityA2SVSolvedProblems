if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i in arr:
        if arr[0]!=i:
            print(i)
            break
