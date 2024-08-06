import sys

S = sys.stdin.readline().rstrip()
suffix = ""
arr = set()
for c in S[::-1]:
    suffix = c + suffix
    arr.add(suffix)

print("\n".join(sorted(arr)))
