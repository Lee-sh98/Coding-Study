import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
town = [0]*(N+1)

for _ in range(Q):
    cur = q = int(input())
    mem = -1
    
    while cur > 1:
        if town[cur]:
            mem = cur
        cur //= 2

    if mem != -1:
        print(mem)
    else:
        print(0)
        town[q] = 1
