import sys
input = sys.stdin.readline

def solve():
    for i in range(1, N+1):
        if stack[books[i]][-1] == i:
            stack[books[i]].pop()
        else:
            return 'No'
    return 'Yes'

N, M = map(int, input().split())
books = [0]*(N+1)
stack = []
for i in range(M):
    k = int(input())
    stack.append(list(map(int, input().split())))
    for book in stack[-1]:
        books[book] = i
print(solve())
