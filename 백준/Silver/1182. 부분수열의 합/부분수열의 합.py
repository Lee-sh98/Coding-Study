import sys
input = sys.stdin.readline

def sub_seq(total, pos, count):
    global result
    if count>N:
        return
    if 0<count<=N and total == S:
        result += 1
    for i in range(pos, N):
        sub_seq(total + arr[i], i+1, count+1)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

sub_seq(0, 0, 0)

print(result)
