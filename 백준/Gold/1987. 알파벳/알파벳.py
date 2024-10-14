import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
A = ord('A')

def solve(x, y):
    result = 0
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if not(0<=nx<R and 0<=ny<C):
            continue
        idx = ord(arr[nx][ny])-A
        if not used[idx]:
            used[idx] = True
            result = max(result, solve(nx, ny))
            used[idx] = False
    return result+1

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
used = [False]*26
used[ord(arr[0][0]) - A] = True

result = solve(0, 0)
print(result)
