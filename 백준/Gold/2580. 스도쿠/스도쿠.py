import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
rows = [[False]*9 for _ in range(9)]
cols = [[False]*9 for _ in range(9)]
rects = [[False]*9 for _ in range(9)]
blanks = []

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blanks.append((i, j))
        else:
            rows[i][arr[i][j]-1] = True
            cols[j][arr[i][j]-1] = True
            rects[(i//3*3)+(j//3)][arr[i][j]-1] = True

def check(x, y, a):
    return not(rows[x][a]) and not(cols[y][a]) and not(rects[(x//3*3)+(y//3)][a])

def dfs(idx):
    if idx == len(blanks):
        for a in arr:
            print(" ".join(map(str, a)))
        exit(0)

    x, y = blanks[idx]
    
    for i in range(9):
        if check(x, y, i):
            arr[x][y] = i+1
            rows[x][i] = True
            cols[y][i] = True
            rects[(x//3*3)+(y//3)][i] = True
            dfs(idx+1)
            arr[x][y] = 0
            rows[x][i] = False
            cols[y][i] = False
            rects[(x//3*3)+(y//3)][i] = False

dfs(0)
