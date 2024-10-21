import sys
input = sys.stdin.readline

color = set()

for _ in range(15):
    color |= set(input().split())


result = list(color-set(list("royp")))[0]

match result:
    case 'w':
        print("chunbae")
    case 'b':
        print("nabi")
    case 'g':
        print("yeongcheol")
