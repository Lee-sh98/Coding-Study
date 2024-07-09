import sys
input = sys.stdin.readline

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3]
for c in cost:
    tmp = []
    for i in range(3):
        tmp.append(c[i] + min(dp[-1][:i]+dp[-1][i+1:]))
    dp.append(tmp)

print(min(dp[-1]))
