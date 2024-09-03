import sys
input = sys.stdin.readline

burger = min(int(input()) for _ in range(3))
beverage = min(int(input()) for _ in range(2))

print(burger+beverage-50)
