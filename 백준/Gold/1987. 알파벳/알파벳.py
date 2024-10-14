import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
A = ord('A')

def solve(x, y, mask, count):
    global result
    result = max(result, count)
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if not(0<=nx<R and 0<=ny<C):
            continue
        
        nmask = 1 << ord(arr[nx][ny]) - A
        if not mask & nmask:
            solve(nx, ny, mask|nmask, count+1)

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0

solve(0, 0, 1<<ord(arr[0][0])-A, 1)
print(result)
