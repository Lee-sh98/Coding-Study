import sys
input = sys.stdin.readline

N, T, P = map(int, input().split())

if N == 0:
    print(1)
else:
    arr = list(map(int, input().split()))

    if N==P and arr[-1]>=T:
        print(-1)
    else:
        rank = 1
        for i in range(N):
            if arr[i]<=T:
                break
            rank+=1
        print(rank)
        
