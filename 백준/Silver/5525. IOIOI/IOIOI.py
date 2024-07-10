import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

PN = "I"+"OI"*N
result = 0
for i in range(len(S)-2*N+1):
    cur = S[i:i+2*N+1]
    if cur==PN:
        result += 1
print(result)
