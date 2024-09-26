import sys
input = sys.stdin.readline

def make_tree():
    children = [[] for _ in range(N+1)]
    stack = [1]
    while stack:
        cur = stack.pop()

        for node in edges[cur]:
            if not children[node]:
                children[cur].append(node)
                stack.append(node)
    return children

N, W = map(int, input().split())
water = [0]*(N+1)
water[1] = W
edges = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())
    edges[U].append(V)
    edges[V].append(U)

children = make_tree()

count = 0
for i in range(1, N+1):
    if not children[i]:
        count += 1

print(W/count)
