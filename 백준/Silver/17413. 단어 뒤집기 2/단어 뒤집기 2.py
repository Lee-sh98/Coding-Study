import sys

class Tag:
    def __init__(self, value):
        self.value = value

    def parse(self):
        return "".join(self.value)

class Word:
    def __init__(self, value):
        self.value = value

    def parse(self):
        return " ".join(map(lambda x: x[::-1], self.value.split()))
    

s = sys.stdin.readline().rstrip()
i, n = 0, len(s)
result = []
stack = ""
words = []
while i < n:
    if s[i] == "<":
        if stack:
            word = Word(stack)
            result.append(word)
            stack = ""
        v = ""
        while s[i] != ">":
            v += s[i]
            i += 1
        v += s[i]
        tag = Tag(v)
        result.append(tag)
    else:
        stack += s[i]
    i += 1

if stack:
    word = Word(stack)
    result.append(word)

answer = ""
for r in result:
    answer += r.parse()

print(answer)
