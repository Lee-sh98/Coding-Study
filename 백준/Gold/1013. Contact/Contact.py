import sys, re
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    S = input().rstrip()
    print(("YES","NO")[not re.fullmatch(r"(100+1+|01)+",S)])