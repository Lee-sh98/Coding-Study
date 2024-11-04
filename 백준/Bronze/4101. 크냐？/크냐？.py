import sys
input = lambda: map(int, sys.stdin.readline().split())

while True:
    i, j = input()
    if i==j==0:
        break
    print(("No", "Yes")[i>j])
