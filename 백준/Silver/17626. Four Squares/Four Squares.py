import sys
from math import sqrt
from itertools import combinations_with_replacement as cwr

n = int(sys.stdin.readline())
square = list(map(int(2).__rpow__, range(1, int(sqrt(n))+1)))
double_square = list(map(sum, cwr(square, 2)))

def solution(n):
    if n in square:
        return 1
    elif n in double_square:
        return 2
    else:
        for ds in double_square:
            if n-ds in square:
                return 3
    return 4

print(solution(n))
