import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def solve(c):
    if not c:
        return 0
    if c==S:
        return 1
    elif c[-1] == 'A':
        return solve(c[:-1])
    else:
        return solve(c[:-1][::-1])

S = input().rstrip()
T = input().rstrip()

result = solve(T)
print(result)
