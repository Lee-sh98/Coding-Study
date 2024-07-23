import sys
from collections import defaultdict
input = sys.stdin.readline

def find_anscestors(parent, child):
    result = [child]
    while parent[child] != child:
        result.append(parent[child])
        child = parent[child]
    return result

def find_NCA(p1, p2):
    NCA = p1[-1]
    for a, b in zip(p1[::-1], p2[::-1]):
        if a==b:
            NCA = a
        else:
            break
    return NCA

def solution():
    N = int(input())
    edges = defaultdict(set)
    parent = list(range(N+1))
    
    for _ in range(N-1):
        A, B = map(int, input().split())
        parent[B] = A
    c1, c2 = map(int, input().split())

    p1 = find_anscestors(parent, c1)
    p2 = find_anscestors(parent, c2)
    
    print(find_NCA(p1, p2))


T = int(input())

for _ in range(T):
    solution()
