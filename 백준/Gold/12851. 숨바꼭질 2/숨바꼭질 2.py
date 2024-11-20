from heapq import *
MAX = 100_001
N, K = map(int,input().split())
distances = [MAX]*MAX
distances[N]=0
result = 0
functions = [int(1).__add__, int(-1).__add__, int(2).__mul__]

q = [(0, N)]
while q:
    dist, cur = heappop(q)
    if distances[cur] < dist:
        continue
    if cur == K:
        result += 1
        continue

    for f in functions:
        nxt = f(cur)
        if 0<=nxt<MAX:
            if dist+1 < distances[nxt]:
                reuslt = 0
            if dist+1 <= distances[nxt]:
                distances[nxt] = dist+1
                heappush(q, (dist+1, nxt))
print(distances[K])
print(result)