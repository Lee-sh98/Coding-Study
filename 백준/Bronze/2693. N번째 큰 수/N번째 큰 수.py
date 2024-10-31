import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    print(list(sorted(map(int, input().split())))[-3])
