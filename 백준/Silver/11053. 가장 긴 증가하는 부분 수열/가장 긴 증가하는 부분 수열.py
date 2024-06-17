# 11053 Longest Increasing Subsequence
import sys
input = sys.stdin.readline

def bis(arr, target):
    left, right = 0, len(arr)-1

    while left<=right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

n = int(input())
arr = list(map(int, input().split()))
dp = [1]
result = [arr[0]]

for i in range(n):
    if arr[i]>result[-1]:
        dp.append(dp[-1]+1)
        result.append(arr[i])
    else:
        idx = bis(result, arr[i])
        result[idx] = arr[i]
print(len(result))
