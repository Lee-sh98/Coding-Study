import sys
input = sys.stdin.readline

def find_index(arr, target):
    left, right = 0, len(arr)-1

    while left<=right:
        mid = (left+right)//2

        if arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return left

N = int(input())
arr = list(map(int, input().split()))
answer = [arr[0]]

for a in arr:
    if answer[-1] < a:
        answer.append(a)
    else:
        idx = find_index(answer, a)
        answer[idx] = a

print(len(answer))
