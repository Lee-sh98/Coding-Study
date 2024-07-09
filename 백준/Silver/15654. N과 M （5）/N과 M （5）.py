import sys
input = sys.stdin.readline

def dfs(arr, acc, m):
    if m==0:
        print(*acc, sep=" ")
    else:
        for i in range(len(arr)):
            dfs(arr[:i]+arr[i+1:], acc+[arr[i]], m-1)


N, M = map(int, input().split())
arr = sorted(map(int, input().split()))
dfs(arr, [], M)
