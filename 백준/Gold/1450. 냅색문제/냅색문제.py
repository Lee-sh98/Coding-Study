import sys
from itertools import combinations
input = sys.stdin.readline

def combination_sum(arr, c):
    result = []
    for i in range(1, len(arr)+1):
        for com in combinations(arr, i):
            s = sum(com)
            if s<=c:
               result.append(s)
    return result

N, C = map(int, input().split())
arr = list(map(int, input().split()))

a_list, b_list = arr[:N//2], arr[N//2:]
a_sum = combination_sum(a_list, C)
b_sum = combination_sum(b_list, C)
b_sum.sort()
result = 1

for a in a_sum:
    left, right = 0, len(b_sum)-1

    while left<=right:
        mid = (left+right)//2
        if a + b_sum[mid] <= C:
            left = mid + 1
        else:
            right = mid - 1
    result += left

print(len(a_sum) + len(b_sum) + result)
