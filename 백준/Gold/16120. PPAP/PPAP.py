import sys

S = sys.stdin.readline().rstrip()
stack = []
ppap = list("PPAP")

for c in S:
    stack.append(c)

    while stack[-4:] == ppap:
        stack.pop()
        stack.pop()
        stack.pop()

if stack == ["P"]:
    print("PPAP")
else:
    print("NP")
