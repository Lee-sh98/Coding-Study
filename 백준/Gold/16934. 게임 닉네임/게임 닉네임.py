import sys
input = sys.stdin.readline

class Node:
    def __init__(self, v):
        self.v = v
        self.children = {}
        self.count = 0
        self.is_leaf = False
        

class Trie:
    def __init__(self):
        self.root = Node("")
        self.nicknames = []

    def insert(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = Node(w)
            cur = cur.children[w]
        cur.count += 1
        cur.is_leaf = True
        self.nicknames.append(self.inspect(word))
        

    def inspect(self, word):
        prefix = word[0]
        infix = ""
        cur = self.root.children[prefix]
        for w in word[1:]:
            infix += w
            if len(cur.children) > 1 or cur.is_leaf:
                prefix += infix
                infix = ""
            cur = cur.children[w]
        if cur.children or cur.count > 1:
            prefix += infix + (str(cur.count) if cur.count>1 else "")
        return prefix
        


N = int(input())
trie = Trie()

for _ in range(N):
    name = input().rstrip()
    trie.insert(name)

for nickname in trie.nicknames:
    print(nickname)
