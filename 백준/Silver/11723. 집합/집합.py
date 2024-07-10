import sys
input = sys.stdin.readline

M = int(input())
s = set()

def operation(s, commend, x=None):
    match commend:
        case "add":
            s.add(x)
        case "remove":
            s.discard(x)
        case "check":
            print(int(x in s))
        case "toggle":
            s.discard(x) if x in s else s.add(x)
        case "all":
            s.update(range(1, 21))
        case "empty":
            s.clear()


for _ in range(M):
    commend, *x = input().split()
    
    operation(s, commend, *map(int, x))

