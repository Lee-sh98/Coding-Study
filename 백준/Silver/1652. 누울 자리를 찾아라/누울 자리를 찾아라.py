import sys
input = sys.stdin.readline

def solve(iterable):
    result = 0
    for i in iterable:
        cnt = 0
        for j in i:
            if j == '.':
                cnt += 1
            else:
                cnt = 0
            if cnt==2:
                result += 1
    return result

N = int(input())
graph = [input().rstrip() for _ in range(N)]
h, v = solve(graph), solve(map("".join, zip(*graph)))
print(h, v)
