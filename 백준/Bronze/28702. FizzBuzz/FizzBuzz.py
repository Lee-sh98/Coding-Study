import sys
input = sys.stdin.readline

i = input().rstrip()
j = input().rstrip()
k = input().rstrip()
base = 0
if i.isdecimal():
    base = int(i)
elif j.isdecimal():
    base = int(j)-1
elif k.isdecimal():
    base = int(k)-2

target = base + 3
fizz, buzz = "Fizz", "Buzz"
print(f"{fizz if target%3==0 else ''}{buzz if target%5==0 else ''}{target if target%3 and target%5 else ''}")
