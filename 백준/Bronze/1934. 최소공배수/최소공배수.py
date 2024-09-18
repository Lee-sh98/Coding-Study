import sys
from math import lcm
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))
