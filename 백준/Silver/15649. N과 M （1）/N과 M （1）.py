import copy

N, M = map(int, input().split())

def dfs(arr, acc, used, m):
    if not m:
        print(*acc, sep=" ")
    for i in arr:
        if used[i]:
            continue
        next_used = copy.deepcopy(used)
        next_used[i] = 1
        dfs(arr, acc+[i], next_used, m-1)
        
arr = list(range(1, N+1))
dfs(arr, [], [0]*(N+1),M)
