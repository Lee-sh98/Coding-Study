import sys
input = sys.stdin.readline

def ROT13(c):
    if c.isalpha():
        if c.isupper():
            return chr(ord('A')+(ord(c)-ord('A')+13)%26)
        else:
            return chr(ord('a')+(ord(c)-ord('a')+13)%26)
    else:
        return c

print("".join(map(ROT13, input().rstrip())))
