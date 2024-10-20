import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
sec = A*3600+B*60+C+int(input())

H, r = divmod(sec, 3600)
M, S = divmod(r, 60)
print(H%24, M, S)
