import sys
input = lambda: sys.stdin.readline().rstrip()

print(("go", "no")[len(input())<len(input())])
