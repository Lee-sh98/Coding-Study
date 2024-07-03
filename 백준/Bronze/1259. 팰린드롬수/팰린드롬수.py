import sys
input = sys.stdin.readline

while (s:=input().rstrip()) != "0":
    print(("no","yes")[s==s[::-1]])
