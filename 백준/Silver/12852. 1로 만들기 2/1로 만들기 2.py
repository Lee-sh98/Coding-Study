import sys
sys.setrecursionlimit(10**7)

def solve(n, c):
    count[n] = c
    if n%3 == 0 and c+1 < count[n//3]:
        parent[n//3] = n
        solve(n//3, c+1)

    if n%2 == 0 and c+1 < count[n//2]:
        parent[n//2] = n
        solve(n//2, c+1)
        
    if 1< n and c + 1< count[n-1]:
        parent[n-1] = n
        solve(n-1, c+1)

N = int(sys.stdin.readline())
parent = [0]*(N+1)
count = [N]*(N+1)

solve(N, 0)

print(count[1])
result = [str(1)]
cur = 1
while cur != N:
    cur = parent[cur]
    result.append(str(cur))
print(" ".join(result[::-1]))
