import sys, heapq
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    result = 0
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    dq = deque(enumerate(arr))
    hq = [(-i, i) for i in arr]
    heapq.heapify(hq)
    
    while dq:
        idx, cur = dq.popleft()
        _, h = heapq.heappop(hq)
        if cur==h:
            result+=1
            if idx==M:
                print(result)
                break
        else:
            dq.append([idx, cur])
            heapq.heappush(hq, (-h, h))
