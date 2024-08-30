import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
value = [" "]+[chr(i+ord('A')) for i in range(26)]+[chr(j+ord('a')) for j in range(26)]
key = dict(zip(value, range(53))) 

secret = [0]*53
plain = [0]*53

for i in map(int, input().split()):
    secret[i] += 1

for j in input().rstrip():
    plain[key[j]] += 1

print(("n","y")[secret == plain])
