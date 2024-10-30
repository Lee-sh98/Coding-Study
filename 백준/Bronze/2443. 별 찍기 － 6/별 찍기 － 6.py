import sys

N = int(sys.stdin.readline())
print("\n".join(" "*i+"*"*(2*N-2*i-1) for i in range(N)))
