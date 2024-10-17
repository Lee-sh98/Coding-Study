import sys
from collections import deque
from itertools import permutations
input = sys.stdin.readline

def solve(arr):
    q = deque([(arr, 0)])
    
    while q:
        scv, count = q.popleft()
        if not any(scv):
            return count

        for per in pers[len(scv)-1]:
            attacked = map(int.__sub__, scv, per)
            remains = tuple(sorted(filter(int(0).__lt__, attacked)))
            if remains not in visited:
                visited.add(remains)
                q.append((remains, count+1))

N = int(input())
x, y, z = SCV = list(map(int, input().split()))+[0]*(3-N)
visited = set()
damage = [9, 3, 1]
pers = [list(permutations(damage[:i], i)) for i in range(1, 4)]

result = solve(SCV)
print(result)
