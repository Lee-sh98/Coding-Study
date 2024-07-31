import sys

N, B = map(int, sys.stdin.readline().split())
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ""

while N:
    res += str(arr[N%B])
    N //= B

print(res[::-1])
