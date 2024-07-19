import sys
input = sys.stdin.readline

def dfs(acc, s):
    if len(acc) == 6:
        print(*acc)
    else:
        for i in range(len(s)):
            dfs(acc+[s[i]], s[i+1:])

flag = False
while (arr:=list(map(int, input().split()))) != [0]:
    if flag:
        print()
    result = []
    k, s = arr[0], arr[1:]
    dfs([], s)
    flag = True
