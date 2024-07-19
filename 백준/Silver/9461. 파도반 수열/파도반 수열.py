import sys
input = sys.stdin.readline

def memo(func):
    mem = {}
    def helper(n):
        if n not in mem:
            mem[n] = func(n)
        return mem[n]
    return helper

def padovan(n):
    if n<4:
        return 1
    return padovan(n-2) + padovan(n-3)

padovan = memo(padovan)

T = int(input())
for _ in range(T):
    print(padovan(int(input())))
