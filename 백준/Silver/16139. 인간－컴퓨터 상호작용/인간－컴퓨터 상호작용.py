import sys
input = sys.stdin.readline

S = input().rstrip()
q = int(input())
alpha = {chr(i+ord('a')):[0] for i in range(26)}

for i, s in enumerate(S):
    alpha[s] += [alpha[s][-1]]*(i-len(alpha[s])+1) + [alpha[s][-1]+1]

for i in range(26):
    c = chr(i+ord('a'))
    alpha[c] += [alpha[c][-1]]*(len(S)-len(alpha[c])+1)

for _ in range(q):
    a, l, r = input().split()
    l_num, r_num = int(l), int(r)
    print(alpha[a][r_num+1] - alpha[a][l_num])
