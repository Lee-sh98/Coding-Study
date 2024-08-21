import sys
input = sys.stdin.readline
    
N = int(input())
parents = list(map(int, input().split()))
removal = int(input())

children = [[] for _ in range(N)]
for child, parent in enumerate(parents):
    if child == removal or parent == removal:
        continue
    if parent==-1:
        continue
    children[parent].append(child)

root = parents.index(-1)
stack = [root]
leafNodes = [0]*N

while stack:
    cur = stack.pop()
    
    if cur == removal:
        continue
    if not children[cur]:
        leafNodes[cur] = 1

    for child in children[cur]:
        stack.append(child)

print(sum(leafNodes))
