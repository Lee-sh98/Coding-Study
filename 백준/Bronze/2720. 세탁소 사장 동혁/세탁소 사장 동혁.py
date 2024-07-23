import sys
input = sys.stdin.readline

T = int(input())
unit = [25, 10, 5, 1]

for _ in range(T):
    money = int(input())
    cur = 0
    exchange = [0]*4
    
    for i, u in enumerate(unit):
        exchange[i] = money//u
        money %= u
    print(*exchange)
