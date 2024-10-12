import sys
from itertools import combinations
input = sys.stdin.readline
INF = float('inf')

N = int(input())
arr= [list(map(int, input().split())) for _ in range(N)]
S = sum(map(sum, arr))
result = INF

for com in combinations(range(N), N//2):
    A, B = 0, 0
    
    for i, j in combinations(com, 2):
        A += arr[i][j] + arr[j][i]
    for k, l in combinations(set(range(N))-set(com), 2):
        B += arr[k][l] + arr[l][k]
    result = min(result, abs(A-B))

print(result)
