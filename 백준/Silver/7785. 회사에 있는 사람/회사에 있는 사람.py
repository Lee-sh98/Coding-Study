import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
s = set()
action = {"enter":s.add,
          "leave": s.discard}
for _ in range(n):
    name, commend = input().split()
    action[commend](name)

for v in sorted(s, reverse=True):
    print(v+'\n')
