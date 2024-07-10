import sys
input = sys.stdin.readline

def dfs(arr, acc, m):
    if m==0:
        print(*acc)
    else:
        for i in range(len(arr)):
            dfs(arr[i:], acc+[arr[i]], m-1)

N, M = map(int, input().split())
arr = list(set(map(int, input().split())))
arr.sort()
dfs(arr, [], M)
