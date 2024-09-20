import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
columns = defaultdict(int)
for i in range(N):
    L, H = map(int, input().split())
    columns[L] = H

left, right = min(columns), max(columns)
stack = [0]*1001
for i in columns:
    stack[i-left] = columns[i]

MAX = stack.pop()
result = MAX
tmp = []
while stack:
    cur = stack.pop()
    if cur > MAX:
        result += len(tmp)*MAX
        MAX = cur
        tmp = []
    tmp.append(cur)

MAX = tmp.pop()
result += MAX
while tmp:
    MAX = max(MAX, tmp.pop())
    result += MAX

print(result)
