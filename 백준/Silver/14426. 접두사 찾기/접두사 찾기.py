import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False
    

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_end = True
        
    def inspect(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

N, M = map(int, input().split())
S = list(input().rstrip() for _ in range(N))
target = list(input().rstrip() for _ in range(M))
count = 0
trie = Trie()

for s in S:
    trie.insert(s)

for t in target:
    if trie.inspect(t):
        count += 1

print(count)
