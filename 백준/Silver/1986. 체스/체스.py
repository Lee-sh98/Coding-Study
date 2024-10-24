import sys
input = sys.stdin.readline

def in_board(x, y):
    return 0<=x<n and 0<=y<m

knight_x = [-1, -2, -2, -1, 1, 2, 2, 1]
knight_y = [2, 1, -1, -2, -2, -1, 1, 2]

queen_x = [0, -1, -1, -1, 0, 1, 1, 1]
queen_y = [1, 1, 0, -1, -1, -1, 0, 1]

n, m = map(int, input().split())
board = [["O"]*m for _ in range(n)]
Q, *queens = map(int, input().split())
K, *knights = map(int, input().split())
P, *pawns = map(int, input().split())

for i in range(P):
    x, y = pawns[2*i]-1, pawns[2*i+1]-1
    board[x][y] = "P"

for j in range(K):
    x, y = knights[2*j]-1, knights[2*j+1]-1
    board[x][y] = "K"

    for dx, dy in zip(knight_x, knight_y):
        nx, ny = x+dx, y+dy
        if not in_board(nx, ny):
            continue
        if board[nx][ny] == "O":
            board[nx][ny] = "A"

for k in range(Q):
    x, y = queens[2*k]-1, queens[2*k+1]-1
    board[x][y] = "Q"
    
    for dx, dy in zip(queen_x, queen_y):
        nx, ny = x+dx, y+dy
        while in_board(nx, ny) and board[nx][ny] in ["O", "A"]:
            board[nx][ny] = "A"
            nx += dx
            ny += dy

print(sum(b.count('O') for b in board))
