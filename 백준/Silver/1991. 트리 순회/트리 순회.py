import sys
input = sys.stdin.readline

class Node:
    def __init__(self, v, l, r):
        self.v = v
        self.left = None if l == "." else Node(l, ".", ".")
        self.right = None if r == "." else Node(r, ".", ".")
    
        
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, node, cur):
        if cur== None and self.root==None:
            self.root= node
            return
        
        if cur and cur.left:
            self.insert(node, cur.left)
        if cur and cur.right:
            self.insert(node, cur.right)

        if cur.left and cur.left.v == node.v:
            cur.left = node
        if cur.right and cur.right.v == node.v:
            cur.right = node
        

    def preorder(self, cur=None):
        if cur==None:
            cur=self.root

        print(cur.v, end="")
        if cur.left:
            self.preorder(cur.left)
        if cur.right:
            self.preorder(cur.right)

    def inorder(self, cur=None):
        if cur==None:
            cur=self.root
        if cur.left:
            self.inorder(cur.left)
        print(cur.v, end="")
        if cur.right:
            self.inorder(cur.right)

    def postorder(self, cur=None):
        if cur==None:
            cur=self.root

        if cur.left:
            self.postorder(cur.left)
        if cur.right:
            self.postorder(cur.right)
        print(cur.v, end="")

N = int(input())
t = Tree()

for _ in range(N):
    node = Node(*input().split())
    
    t.insert(node, t.root)

t.preorder()
print()
t.inorder()
print()
t.postorder()
