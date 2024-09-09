import sys
input = sys.stdin.readline

N = int(input())
children = [[-1, -1] for _ in range(N+1)]
is_root = [True]*(N+1)
is_root[0] = False

for _ in range(N):
    n, l, r = map(int, input().split())

    if l != -1:
        is_root[l] = False
    if r != -1:
        is_root[r] = False
    
    children[n] = [l, r]

root = is_root.index(True)
cur = root
cnt = 0
while children[cur][1] != -1:
    cnt += 1
    cur = children[cur][1]

print(2*(N-1)-cnt)
