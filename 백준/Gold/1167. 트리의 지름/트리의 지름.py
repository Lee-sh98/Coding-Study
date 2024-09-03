import sys
input = sys.stdin.readline

def dfs(root):
    cost = [-1]*(V+1)
    stack = [(root, 0)]
    
    while stack != []:
        cur, dist = stack.pop()
        cost[cur] = (cur, dist)
        for node, next_dist in adj[cur]:
            if cost[node] == -1:
                stack.append((node, dist+next_dist))
    return max(cost[1:], key=lambda x: x[1])

V = int(input())

adj = {}
for _ in range(V):
    node, *child, _ = map(int, input().split())

    adj[node] = [(child[i], child[i+1]) for i in range(0, len(child), 2)]

tmp_node, _ = dfs(1)
_, result = dfs(tmp_node)
print(result)
