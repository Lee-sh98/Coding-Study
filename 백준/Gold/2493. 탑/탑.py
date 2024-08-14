import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
result = [0]*N

for i in range(N-1, -1, -1):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = i+1
    stack.append(i)

print(" ".join(map(str, result)))
