import sys
input = sys.stdin.readline

n = int(input())
s = set()
action = {"enter":s.add,
          "leave": s.discard}
for _ in range(n):
    name, commend = input().split()
    action[commend](name)

print(*sorted(s, reverse=True), sep="\n")
