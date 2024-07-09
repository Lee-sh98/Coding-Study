import sys
input = sys.stdin.readline

K = int(input())
stack = []
operation = {0: stack.append, 1: stack.pop}

for _ in range(K):
    x = int(input())
    operation[x==0]((x, -1)[x==0])

print(sum(stack))
