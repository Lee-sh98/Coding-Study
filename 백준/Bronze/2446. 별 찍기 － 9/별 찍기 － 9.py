import sys

N = int(sys.stdin.readline())
M = 2*N-2
print("\n".join(" "*((M-abs(n))//2)+"*"*(abs(n)+1) for n in range(-M, M+1, 2)))
