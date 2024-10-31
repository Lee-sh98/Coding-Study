import sys
input = sys.stdin.readline

def bs(arr, target):
    l, r = 0, len(arr)-1

    while l<=r:
        mid = (l+r)//2
        if arr[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return l

N = int(input())
arr = list(map(int, input().split()))
arr.reverse()

answer = [arr[0]]
for a in arr[1:]:
    if answer[-1] < a:
        answer.append(a)
    else:
        idx = bs(answer, a)
        answer[idx] = a

print(N-len(answer))
