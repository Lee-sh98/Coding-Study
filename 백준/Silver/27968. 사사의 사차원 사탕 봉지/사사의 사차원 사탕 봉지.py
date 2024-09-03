import sys
input = sys.stdin.readline

def bs(target, left, right):
    if left>right:
        return "Go away!"
    mid = (left+right)//2
    
    if acc[mid]>=target>acc[mid-1]:
        return mid
    elif acc[mid]>target:
        return bs(target, left, mid-1)
    else:
        return bs(target, mid+1, right)
    

N, M = map(int, input().split())
arr = list(map(int, input().split()))
acc = [0]*(M+1)
for i in range(M):
    acc[i+1] = acc[i]+arr[i]

max_candy = acc[-1]
for _ in range(N):
    B = int(input())
    if max_candy>=B:
        result = bs(B, 0, M+1)
        print(result)
    else:
        print("Go away!")
