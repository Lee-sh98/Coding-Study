import sys
from collections import defaultdict
input = sys.stdin.readline


def inorder(node, depth, parent_left):
    level[depth].append(node)

    left, right = children[node]
    left_size, right_size = 0, 0
    
    if left != -1:
        left_size = inorder(left, depth+1, parent_left)
    if right != -1:
        right_size = inorder(right, depth+1, parent_left+left_size+1)
    position[node] = parent_left + left_size + 1
    return left_size + right_size + 1

N = int(input())
children = [[-1, -1] for _ in range(N+1)]
is_root = [True]*(N+1)
is_root[0] = False
position = [0]*(N+1)
level = defaultdict(list)

for _ in range(N):
    n, l, r = map(int, input().split())
    if l!= -1:
        is_root[l] = False
    if r != -1:
        is_root[r] = False
    children[n] = [l, r]
root = is_root.index(True)
inorder(root, 1, 0)
max_level = 0
max_width = 0
ans = []

for lev, nodes in sorted(level.items()):
    left = min(map(lambda x: position[x], nodes))
    right = max(map(lambda y: position[y], nodes))

    width = right-left+1
    if max_width < width:
        max_level = lev
        max_width = width
    ans.append((lev, width))
print(max_level, max_width)

