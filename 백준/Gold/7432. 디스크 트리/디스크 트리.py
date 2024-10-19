import sys
input = sys.stdin.readline

class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.is_leaf = False
        
class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, words):
        cur = self.root
        for word in words:
            if word not in cur.children:
                cur.children[word] = Node(word)
            cur = cur.children[word]

    def inspect(self):
        stack = [(self.root.children[v], 0) for v in sorted(self.root.children, reverse=True)]

        while stack:
            cur, depth = stack.pop()
            print(" "*depth+cur.name)
            for child in sorted(cur.children, reverse=True):
                stack.append((cur.children[child], depth+1))

N = int(input())
trie = Trie()

for _ in range(N):
    file = input().rstrip()
    trie.insert(file.split('\\'))

trie.inspect()
