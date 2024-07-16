import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())
alpha = {i:[0]*(len(S)+1) for i in range(26)}

for i, s in enumerate(S):
    for j in range(26):
        alpha[j][i+1] = alpha[j][i] + int(ord(s)-ord('a')==j)
for _ in range(q):
    a, l, r = input().split()
    a_num = ord(a) - ord('a')
    l_num, r_num = int(l), int(r)
    print(alpha[a_num][r_num+1] - alpha[a_num][l_num])
