import sys
input = sys.stdin.readline

def dfs(acc, arr):
    if sum(acc) == 100 and len(acc)==7:
        result.append(acc)
    elif len(acc)<7:
        for i in range(len(arr)):
            dfs(acc+[arr[i]], arr[i+1:])

dwarf = [int(input()) for _ in range(9)]
result = []
dfs([], dwarf)

print(*sorted(result[0]), sep="\n")
