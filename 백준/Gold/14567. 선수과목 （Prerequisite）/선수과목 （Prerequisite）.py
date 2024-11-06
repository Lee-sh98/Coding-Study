import sys
input = lambda: map(int, sys.stdin.readline().split())

N, M = input()
children = [[] for _ in range(N)]
answer = [1]*N

for _ in range(M):
    A, B = input()
    children[A-1].append(B-1)

for i in range(N):
    for child in children[i]:
        answer[child] = max(answer[child], answer[i]+1)
        
print(" ".join(map(str, answer)))
