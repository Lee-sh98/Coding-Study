import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
S = input().rstrip()
dp = [INF]*N
dp[0] = 0
idx = {c:[] for c in "BOJ"}
prev = dict(zip("BOJ", "JBO"))

for i in range(N):
    idx[S[i]].append(i)

for i in range(1, N):
    dp[i] = min((dp[j]+(i-j)*(i-j) for j in idx[prev[S[i]]] if j<i), default=INF)

dp[N-1] += -(dp[N-1]+1)*(dp[N-1]>=INF)
print(dp[N-1])
