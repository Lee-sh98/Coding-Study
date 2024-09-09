import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.is_leaf = False
        self.next = [None]*10

class Trie:
    def __init__(self):
        self.root = Node()
        self.is_consistent = True

    def insert(self, word):
        cur = self.root
        for i in range(len(word)):
            if cur.is_leaf or (i==len(word)-1 and cur.next[word[i]]):
                self.is_consistent = False
                break
            if not cur.next[word[i]]:
                cur.next[word[i]] = Node()
            cur = cur.next[word[i]]
        cur.is_leaf = True

t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    for _ in range(n):
        number = list(map(int, input().rstrip()))
        trie.insert(number)
    print(("NO", "YES")[trie.is_consistent])
