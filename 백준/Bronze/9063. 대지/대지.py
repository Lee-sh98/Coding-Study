import sys
from functools import reduce
input = sys.stdin.readline

N = int(input())

arr = map(list, zip(*(map(int, input().split()) for _ in range(N))))

print(reduce(int.__mul__, map(lambda t: max(t)-min(t), arr)))
