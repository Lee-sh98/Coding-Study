import sys
from collections import deque
input = sys.stdin.readline    

N, S, M = map(int, input().split())
V = list(map(int, input().split()))
dp = [[-1]*(M+1) for _ in range(N)]

q = deque([(0, S)])
while q:
    cur, volume = q.popleft()
    if cur==N:
        continue

    for v in [V[cur], -V[cur]]:
        if 0 <= volume+v <= M and dp[cur][volume+v]==-1:
            dp[cur][volume+v] = volume+v
            q.append((cur+1, volume+v))

print(max(dp[N-1]))
