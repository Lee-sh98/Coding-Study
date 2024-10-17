import sys
input = sys.stdin.readline

def transpose(arr):
    return list(map(list, zip(*arr)))

def horizontal_reverse(arr):
    return list(reversed(arr))

def vertical_reverse(arr):
    return list(map(lambda a: a[::-1], arr))

def right_rotate(arr):
    return vertical_reverse(transpose(arr))

def left_rotate(arr):
    return horizontal_reverse(transpose(arr))

def divide(arr):
    A, B = len(arr), len(arr[0])
    one = [a[:B//2] for a in arr[:A//2]]
    two = [a[B//2:] for a in arr[:A//2]]
    three = [a[:B//2] for a in arr[A//2:]]
    four = [a[B//2:] for a in arr[A//2:]]
    
    return one, two, three, four

def right_turn(arr):
    one, two, three, four = divide(arr)

    return list(map(list.__add__, three, one))+list(map(list.__add__, four, two))

def left_turn(arr):
    one, two, three, four = divide(arr)
    return list(map(list.__add__, two, four))+list(map(list.__add__, one, three))

N, M, R = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]

for commend in map(int, input().split()):
    match commend:
        case 1:
            arr = horizontal_reverse(arr)
        case 2:
            arr = vertical_reverse(arr)
        case 3:
            arr = right_rotate(arr)
        case 4:
            arr = left_rotate(arr)
        case 5:
            arr = right_turn(arr)
        case 6:
            arr = left_turn(arr)

for a in arr:
    print(" ".join(a))
