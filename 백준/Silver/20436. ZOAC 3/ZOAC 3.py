import sys
input = sys.stdin.readline

def is_consonant(c):
    return c in "qwertasdfgzxcv"

def push(current, target):
    cx, cy = position[current]
    tx, ty = position[target]

    return abs(cx-tx)+abs(cy-ty)+1

top = [(0, i) for i in range(10)]
mid = [(1, i) for i in range(9)]
bottom = [(2, i) for i in range(7)]
alpha = "qwertyuiopasdfghjklzxcvbnm"

position = dict(zip(alpha, top+mid+bottom))

left_finger, right_finger = input().split()
result = 0
for c in input().rstrip():
    if is_consonant(c):
        result += push(left_finger, c)
        left_finger = c
    else:
        result += push(right_finger, c)
        right_finger = c

print(result)
    
