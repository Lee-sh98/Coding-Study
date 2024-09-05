import sys
input = sys.stdin.readline

def bs(left, right, target):
    if left>right:
        return 0
    mid = (left+right)//2
    if note_1[mid] == target:
        return 1
    elif note_1[mid] < target:
        return bs(mid+1, right, target)
    else:
        return bs(left, mid-1, target)

T = int(input())
for _ in range(T):
    N = int(input())
    note_1 = list(map(int, input().split()))
    note_1.sort()

    M = int(input())
    note_2 = list(map(int, input().split()))

    for n in note_2:
        print(bs(0, N-1, n))
