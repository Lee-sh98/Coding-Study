import sys
input = sys.stdin.readline

N = int(input())
arr = [(i, int(input())) for i in range(N)]
stack = []
result = [0]*N

for i, a in arr[::-1]:
    while stack and a > stack[-1][1]:
        result[i] += result[stack.pop()[0]]+1
    stack.append((i, a))

print(sum(result))
