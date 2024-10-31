import sys
input = lambda:int(sys.stdin.readline())

print("\n".join(map(str, sorted((input() for _ in range(input())), reverse=True))))
