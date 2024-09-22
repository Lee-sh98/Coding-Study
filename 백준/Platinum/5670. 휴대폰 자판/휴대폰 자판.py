import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = {}
        self.is_leaf = False

class Trie:
    def __init__(self):
        self.root = Node()
        self.count = 0

    def insert(self, word):
        self.count += 1
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = Node()
            cur = cur.children[w]
        cur.is_leaf = True

    def inspect(self):
        result = 0
        stack = []

        for child in self.root.children:
            stack.append((1, self.root.children[child]))

        while stack:
            depth, cur = stack.pop()

            while len(cur.children) == 1 and not cur.is_leaf:
                cur = list(cur.children.values())[0]

            if cur.is_leaf:
                result += depth

            for child in cur.children:
                stack.append((depth+1, cur.children[child]))

        print(f"{result/self.count:.2f}")

while True:
    try:
        N = int(input())
        trie = Trie()
        
        for _ in range(N):
            word = input().rstrip()
            trie.insert(word)
        trie.inspect()
        
    except Exception:
        break
