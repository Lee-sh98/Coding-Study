import sys

S = sys.stdin.readline().rstrip()
count = [0]*26

for c in S:
    count[ord(c)-ord('a')] += 1

print(" ".join(map(str, count)))
