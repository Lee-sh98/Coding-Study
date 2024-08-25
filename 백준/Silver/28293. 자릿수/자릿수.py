import sys
from math import log
a, b = map(int, sys.stdin.readline().split())
result = int((b*log(a, 10))//1 + 1)
print(result)
