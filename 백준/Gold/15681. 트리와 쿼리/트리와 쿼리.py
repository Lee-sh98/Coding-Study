import sys
from collections import defaultdict
input = sys.stdin.readline


def makeTree(root, adj):
    chk = [0]*(N+1)
    queue = [R]
    
    while queue:
        cur = queue.pop()
        chk[cur] = 1
        for i in adj[cur]:
            if not chk[i]:
                parent[i] = cur
                children[cur].append(i)
                chk[i] = 1
                queue.append(i)
    
def countSubtreeNodes(root):
    chk = [0]*(N+1)
    stack = [root]

    while stack:
        cur = stack.pop()
        chk[cur] = 1
        if any(chk[child]==0 for child in children[cur]):
            stack.append(cur)
            stack.extend(children[cur])
            continue
        subtree_size[cur] += 1
        if cur != root:
            subtree_size[parent[cur]] += subtree_size[cur]


N, R, Q = map(int, input().split())
edges = [map(int, input().split()) for _ in range(N-1)]

adj = defaultdict(set)
parent = list(range(N+1))
children = [[] for _ in range(N+1)]
subtree_size = [0]*(N+1)

for U, V in edges:
    adj[U].add(V)
    adj[V].add(U)

makeTree(R, adj)
countSubtreeNodes(R)

for _ in range(Q):
    q = int(input())
    print(subtree_size[q])
