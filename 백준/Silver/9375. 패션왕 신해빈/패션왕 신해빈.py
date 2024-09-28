import sys
from collections import defaultdict
input = sys.stdin.readline

T  = int(input())
for _ in range(T):
    fashion = defaultdict(int)
    n = int(input())

    for _ in range(n):
        name, kind = input().split()
        fashion[kind] += 1

    result = 1
    for count in fashion.values():
        result *= count+1

    print(result - 1)
