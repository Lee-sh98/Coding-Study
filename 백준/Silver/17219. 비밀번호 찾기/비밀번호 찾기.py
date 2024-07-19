import sys
input = sys.stdin.readline

N, M = map(int, input().split())
password = dict(input().split() for _ in range(N))

print(*(password.get(input().rstrip()) for _ in range(M)),sep="\n")
