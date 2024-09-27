import sys
input = sys.stdin.readline

def combination(length, last):
    global v_cnt, c_cnt
    if length == L and v_cnt >= 1 and c_cnt >= 2:
        print("".join(map(arr.__getitem__, filter(chk.__getitem__, range(C)))))
    else:
        for i in range(last, C):
            if arr[i] in vowel:
                v_cnt += 1
            else:
                c_cnt += 1
            chk[i] = 1
            combination(length+1, i+1)
            chk[i] = 0
            if arr[i] in vowel:
                v_cnt -= 1
            else:
                c_cnt -= 1

L, C = map(int, input().split())
vowel = set("aeiou")
v_cnt, c_cnt = 0, 0
arr = list(input().split())
arr.sort()
chk = [0]*C

combination(0, 0)
