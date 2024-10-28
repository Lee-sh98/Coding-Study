import sys
input = sys.stdin.readline

def calc(a, b):
    return sum(map(str.__ne__, a, b))

A, B = input().split()

print(min(map(lambda i: calc(A, B[i:len(B)+i]),range(len(B)-len(A)+1))))
