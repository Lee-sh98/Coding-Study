from collections import Counter

N = int(input())
cards = Counter(input().split())

M = int(input())

print(" ".join(str(cards[num]) for num in input().split()))
