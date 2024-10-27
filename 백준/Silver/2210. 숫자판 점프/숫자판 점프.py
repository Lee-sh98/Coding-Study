import sys
input = sys.stdin.readline

def dfs(x, y, s):
    if len(s) == 6:
        answer.add(s)
        answer.add(s[::-1])
    else:
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0<=nx<5 and 0<=ny<5:
                dfs(nx, ny, s+board[x][y])
    

board = [list(input().split()) for _ in range(5)]
answer = set()
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(answer))
