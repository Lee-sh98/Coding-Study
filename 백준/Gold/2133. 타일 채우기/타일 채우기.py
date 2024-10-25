import sys

N = int(sys.stdin.readline())
acc = ans = 1

for i in range(N//2):
    ans += 2*acc
    acc += ans
print((ans, 0)[N%2])
