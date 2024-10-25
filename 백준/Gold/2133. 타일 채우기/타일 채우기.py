import sys

N = int(sys.stdin.readline())
ans = 1
acc = 1

for i in range(N//2):
    ans = ans + 2*acc
    acc += ans
print((ans, 0)[N%2])
