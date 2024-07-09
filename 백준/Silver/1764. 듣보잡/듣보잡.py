import sys
input = sys.stdin.readline

N, M = map(int, input().split())
unheard = set(input().rstrip() for _ in range(N))
unseen = set(input().rstrip() for _ in range(M))
result = sorted(list(unheard&unseen))
print(len(result))
print(*result, sep="\n")
