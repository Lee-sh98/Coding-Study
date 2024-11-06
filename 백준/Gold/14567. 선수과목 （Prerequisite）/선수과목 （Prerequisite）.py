import sys
input = lambda: map(int, sys.stdin.readline().split())

N, M = input()
children = [[] for _ in range(N)]
stack = []
answer = [0]*N
indegree = [0]*N

for _ in range(M):
    A, B = input()
    children[A-1].append(B-1)
    indegree[B-1] += 1

for i in range(N):
    if indegree[i] == 0:
        stack.append(i)
        answer[i] = 1

while stack:
    cur = stack.pop()

    for child in children[cur]:
        indegree[child] -= 1
        answer[child] = max(answer[child], answer[cur]+1)
        if indegree[child] == 0:
            stack.append(child)

print(" ".join(map(str, answer)))
