import sys
input = sys.stdin.readline

def LCA(A, B):
    if level[A] < level[B]:
        B, A = A, B
    
    while level[A] != level[B]:
        A = parent[A]

    while A!=B:
        A = parent[A]
        B = parent[B]

    return A
    

N, M = map(int, input().split())
children = [[] for _ in range(N+1)]
parent = [-1]*2+[int(input()) for _ in range(N-1)]

for i in range(2, N+1):
    children[parent[i]].append(i)

level = [0]*(N+1)

stack = [(1, 0)]
while stack:
    cur, depth = stack.pop()
    level[cur] = depth

    for child in children[cur]:
        stack.append((child, depth+1))

for _ in range(M):
    B, J = map(int, input().split())
    print(LCA(B, J))
