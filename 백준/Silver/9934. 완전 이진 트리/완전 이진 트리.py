import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(arr, k):
    n = len(arr)
    if n == 1:
        result[k].append(arr[0])
    else:
        solution(arr[:n//2], k+1)
        result[k].append(arr[n//2])
        solution(arr[n//2+1:], k+1)
        

K = int(input())
arr = input().split()
result = defaultdict(list)
solution(arr, 0)

for i in range(K):
    print(" ".join(result[i]))
