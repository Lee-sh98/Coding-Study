import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    M = int(input())
    appearance = [0]*(N)
    for _ in range(M):
        a, b = map(int, input().split())
        appearance[a-1] = 1
        appearance[b-1] = 1

    if all(appearance) and N-1==M:
        print("tree")
    else:
        print("graph")

T = int(input())
for _ in range(T):
    solution()
