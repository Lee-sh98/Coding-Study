import sys
input = sys.stdin.readline

N = int(input())
cards = set(input().split())
M = int(input())
print(*map(lambda x: int(x in cards), input().split()))
