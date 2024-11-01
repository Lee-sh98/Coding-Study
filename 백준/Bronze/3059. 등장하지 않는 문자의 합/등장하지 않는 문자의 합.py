import sys
input = sys.stdin.readline

U = set(map(chr, range(65, 91)))
T = int(input())
for _ in range(T):
    A = set(input().rstrip())
    print(sum(map(ord, U-A)))
