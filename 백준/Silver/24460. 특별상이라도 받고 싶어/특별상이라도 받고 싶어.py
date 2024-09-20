import sys
input = sys.stdin.readline
sys.setrecursionlimit(10_000_000)

def solve(x, y, n):
    if n == 1:
        return arr[x][y]
    else:
        m = n//2
        result = []

        result.append(solve(x, y, m))
        result.append(solve(x, y+m, m))
        result.append(solve(x+m, y, m))
        result.append(solve(x+m, y+m, m))

        return sorted(result)[1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = solve(0, 0, N)
print(result)
