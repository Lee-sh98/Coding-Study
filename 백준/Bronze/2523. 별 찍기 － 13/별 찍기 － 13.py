import sys

N = int(sys.stdin.readline())
print("\n".join("*"*(N-abs(i)) for i in range(-N+1, N)))
