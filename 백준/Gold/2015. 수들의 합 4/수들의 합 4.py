import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
acc = [0]*(N+1)
sum_dict = defaultdict(int)
result = 0

for i, v in enumerate(map(int, input().split())):
    acc[i+1] = acc[i] + v

for i in range(N+1):
    result += sum_dict.get(acc[i]-K, 0)
    sum_dict[acc[i]] += 1

print(result)
