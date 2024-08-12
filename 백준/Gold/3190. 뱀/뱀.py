import sys
from collections import deque

input = sys.stdin.readline

empty = 0
apple = 1
snake = 2

N = int(input())
K = int(input())
board = [[empty]*N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = apple

L = int(input())
controls = {}
for i in range(L):
    t, c = input().split()
    controls[int(t)] = c

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y, d = 0, 0, 0
q = deque([(0, 0)])

play_time = 0
while True:
    x += dx[d]
    y += dy[d]
    play_time += 1
    q.appendleft((x, y))

    if not (0<=x<N and 0<=y<N) or board[x][y] == snake:
        break

    if board[x][y] == empty:
        board[x][y] = snake
        tx, ty = q.pop()
        board[tx][ty] = empty
        
    elif board[x][y] == apple:
        board[x][y] = snake
    
    match controls.get(play_time):
        case "D":
            d = (d + 1)%4
        case "L":
            d = (d - 1)%4

print(play_time)
