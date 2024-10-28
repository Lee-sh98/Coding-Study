import sys
input = lambda: sys.stdin.readline().rstrip()

A, B, C = [input() for _ in range(3)]
print(("NO", "YES")[C in A and C in B])
