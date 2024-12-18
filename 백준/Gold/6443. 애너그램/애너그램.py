import sys
input = sys.stdin.readline

def solution(acc):
    global alpha
    if len(acc)==N:
        result.add(acc)
    else:
        for i in range(26):
            if alpha[i]:
                alpha[i]-=1
                solution(acc+chr(i+ord('a')))
                alpha[i]+=1
    
N=int(input())
for _ in range(N):
    word = input().rstrip()
    N=len(word)
    alpha = [0]*26
    result=set()
    for c in word:
        alpha[ord(c)-ord('a')]+=1
    solution("")
    print("\n".join(sorted(result)))
