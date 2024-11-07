import sys

print(f"{int.__mul__(*map(int, sys.stdin.readline().split()))/2:.1f}")
