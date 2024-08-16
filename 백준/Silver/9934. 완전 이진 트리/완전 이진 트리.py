import sys
input = sys.stdin.readline

def solution(k, left, right):
    mid = (right+left)//2

    if left==right:
        result[k].append(arr[mid])
    elif left<right:
        solution(k+1, left, mid-1)
        result[k].append(arr[mid])
        solution(k+1, mid+1, right)

K = int(input())
arr = input().split()
result = [[] for _ in range(K)]
solution(0, 0, len(arr)-1)

for i in range(K):
    print(" ".join(result[i]))
