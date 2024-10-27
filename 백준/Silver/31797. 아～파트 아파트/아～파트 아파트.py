import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hands = []

for i in range(1, M+1):
    for hand in map(int, input().split()):
        hands.append((hand, i))
hands.sort(key=lambda x:x[0])

print(hands[(N-1)%(2*M)][1])
