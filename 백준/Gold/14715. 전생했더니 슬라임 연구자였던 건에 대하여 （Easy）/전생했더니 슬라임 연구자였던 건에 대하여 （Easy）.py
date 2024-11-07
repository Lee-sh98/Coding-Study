import sys
from math import log2, ceil

K = int(sys.stdin.readline())
n = 2
count = 0

while 1 < K:
    while K%n == 0:
        K//=n
        count += 1
    n += 1

print(ceil(log2(count)))
