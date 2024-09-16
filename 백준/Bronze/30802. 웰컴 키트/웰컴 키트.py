import sys
from math import ceil
input = sys.stdin.readline

N = int(input())
shirts = list(map(int, input().split()))
T, P = map(int, input().split())
print(sum(map(lambda s: ceil(s/T), shirts)))
print(*divmod(N, P))
