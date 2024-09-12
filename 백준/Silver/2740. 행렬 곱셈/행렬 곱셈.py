import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

C = []
for a in A:
    tmp = []
    for b in zip(*B):
        tmp.append(sum(map(int.__mul__, a, b)))
    C.append(tmp)

for c in C:
    print(" ".join(map(str, c)))
