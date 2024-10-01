import sys
from itertools import combinations
input = sys.stdin.readline
MOD = 1_000_000_007

N = int(input())
arr = list(map(int, input().split()))
sum_square = sum(arr)**2
square_sum = sum(map(int(2).__rpow__, arr))
print((sum_square-square_sum)//2%MOD)
