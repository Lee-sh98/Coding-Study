import sys
input = sys.stdin.readline

N = int(input())
operand = {}
postfix = list(input().rstrip())
operation = {"+": float.__add__,
             "-": float.__sub__,
             "*": float.__mul__,
             "/": float.__truediv__}


for i in range(N):
    operand[chr(i+ord("A"))] = float(input())

stack = []
for op in postfix:
    if op in operation:
        x, y = stack.pop(), stack.pop()
        stack.append(operation[op](y, x))
    else:
        stack.append(operand[op])
    
print(f"{stack[-1]:.2f}")
