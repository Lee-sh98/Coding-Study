import sys
input = sys.stdin.readline

class Node:
    def __init__(self, v):
        self.v = v
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node("")

    def insert(self, words: list[str]):
        cur = self.root
        for word in words:
            if word not in cur.children:
                cur.children[word] = Node(word)
            cur = cur.children[word]
        
    def show(self):
        stack = [(-1, self.root)]
        while stack:
            depth, cur = stack.pop()
            if depth>=0:
                print("--"*depth + cur.v)

            for child in sorted(cur.children, reverse=True):
                stack.append((depth+1, cur.children[child]))

N = int(input())
trie = Trie()

for _ in range(N):
    K, *words = input().split()
    trie.insert(words)

trie.show()
        
