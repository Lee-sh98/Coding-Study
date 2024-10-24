import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = [int(input()) for _ in range(M)]
P.sort(reverse = True)

price, profit = 0, 0
for i in range(M):
    cur_profit = P[i]*min(i+1, N)
    if profit <= cur_profit:
        price = P[i]
        profit = cur_profit

print(price, profit)
