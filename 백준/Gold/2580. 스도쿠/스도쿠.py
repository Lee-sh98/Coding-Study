import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
blanks = []

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blanks.append((i, j))

def checkRow(x, a):
    return a not in arr[x]

def checkCol(y, a):
    for j in range(9):
        if a == arr[j][y]:
            return False
    return True

def checkRect(x, y, a):
    nx, ny = x//3*3, y//3*3
    for i in range(nx, nx+3):
        for j in range(ny, ny+3):
            if a==arr[i][j]:
                return False
    return True

def dfs(idx):
    if idx == len(blanks):
        for a in arr:
            print(" ".join(map(str, a)))
        exit(0)

    x, y = blanks[idx]
    
    for i in range(1, 10):
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            arr[x][y] = i
            dfs(idx+1)
            arr[x][y] = 0

dfs(0)
