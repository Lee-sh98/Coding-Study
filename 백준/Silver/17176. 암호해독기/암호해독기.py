import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
value = [" "]+[chr(i+ord('A')) for i in range(26)]+[chr(j+ord('a')) for j in range(26)]
key = dict(zip(range(53), value)) 

secret = map(lambda x: value[int(x)], input().split())
plain = input().rstrip()

secret_count = list(sorted(Counter(secret).items()))
plain_count = list(sorted(Counter(plain).items()))

print(("n","y")[all(map(lambda x, y: x==y, secret_count, plain_count))])
