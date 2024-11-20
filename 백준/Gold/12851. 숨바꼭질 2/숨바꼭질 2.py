from heapq import *
MAX = 100_001
N, K = map(int,input().split())
distances = [MAX]*MAX
distances[N]=0
result = 0

q = [(0, N)]
while q:
    dist, cur = heappop(q)
    if distances[cur] < dist:
        continue
    if cur == K:
        result += 1
        continue

    for nxt in [cur+1, cur-1, 2*cur]:
        if 0<=nxt<MAX and dist+1<=distances[nxt]:
            if dist+1 < distances[nxt]:
                reuslt = 0
            distances[nxt] = dist+1
            heappush(q, (dist+1, nxt))
print(distances[K])
print(result)