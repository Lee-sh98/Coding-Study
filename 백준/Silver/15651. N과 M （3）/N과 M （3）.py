import copy

N, M = map(int, input().split())

def dfs(arr, acc, m):
    if not m:
        print(*acc, sep=" ")
        return
    for i in arr:
        dfs(arr, acc+[i], m-1)
    
arr = list(range(1, N+1))
dfs(arr, [], M)
