import sys
from itertools import combinations
input = sys.stdin.readline

def calculate(com: list) -> int:
    sour_total, bitter_total = sours[com[0]], bitters[com[0]]
    
    for j in com[1:]:
        sour_total *= sours[j]
        bitter_total += bitters[j]
    return abs(sour_total - bitter_total)

N = int(input())
sours, bitters = [0]*N, [0]*N
for i in range(N):
    sours[i], bitters[i] = map(int, input().split())

result = []
for i in range(1, N+1):
    for com in combinations(range(N), i):
        result.append(calculate(com))
print(min(result))
