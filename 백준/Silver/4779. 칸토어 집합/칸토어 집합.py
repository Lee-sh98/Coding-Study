import sys
input = sys.stdin.readline

def memo(func):
    mem = {}
    def helper(n):
        if n not in mem:
            mem[n] = func(n)
        return mem[n]
    return helper

def cantor(n):
    if n==0:
        return "-"
    else:
        return cantor(n-1) + " "*(len(cantor(n-1))) + cantor(n-1)

cantor = memo(cantor)

while (N:=input())!="":
    try:
        N = int(N)
        print(cantor(N))
    except EOFError:
        break
