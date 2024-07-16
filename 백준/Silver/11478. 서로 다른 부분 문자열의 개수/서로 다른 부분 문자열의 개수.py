import sys

substrings = set()
S = input().rstrip()
n = len(S)
for length in range(1, n+1):
    for base in range(n):
        substring = S[base:base+length]
        if len(substring) == length:
            substrings.add(substring)
print(len(substrings))
