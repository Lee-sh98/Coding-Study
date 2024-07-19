import sys
input = sys.stdin.readline

N = int(input())

A = map(int, input().split())
B = map(int, input().split())

S = sum(map(int.__mul__, sorted(A), sorted(B, reverse=True)))
print(S)

