import sys
input = sys.stdin.readline

N, M = map(int, input().split())
password = dict(input().split() for _ in range(N))

for _ in range(M):
    print(password.get(input().rstrip()))
