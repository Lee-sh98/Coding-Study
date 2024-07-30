import sys
input = sys.stdin.readline

r = 31
M = 1234567891

L = int(input())
S = input().rstrip()
result = 0

def unique_number(c):
    return ord(c)-ord('a')+1

for i, c in enumerate(S):
    result += unique_number(c)*pow(r, i, M)

print(result)
