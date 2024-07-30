import sys
import math
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
acc = [0]*N
acc[0] = (1, 1)
for i in range(1, N):
    a, b = acc[i-1]
    g = math.gcd(arr[i-1]*a, arr[i]*b)
    acc[i] = (a*arr[i-1]//g, b*arr[i]//g)
    
for i in acc[1:]:
    print(*i, sep="/")
