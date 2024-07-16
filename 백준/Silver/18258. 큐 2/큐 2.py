import sys
input = sys.stdin.readline

class Node:
    def __init__(self, *v):
        self.v, = v
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.operation = {"push": self.append,
                          "pop": self.pop,
                          "size": self.size,
                          "empty": self.empty,
                          "front": self.front,
                          "back": self.back}

    def action(self, commend, *operand):
        result = self.operation[commend](*operand)
        if commend != "push":
            print(result)
        

    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        
    def pop(self):
        if self.head == None:
            return -1

        result = self.head.v
        self.head = self.head.next

        if self.head == None:
            self.tail = None
        self.length -= 1
        return result

    def size(self):
        return self.length

    def empty(self):
        return int(self.length==0)

    def front(self):
        if self.head == None:
            return -1
        else:
            return self.head.v

    def back(self):
        if self.head == None:
            return -1
        else:
            return self.tail.v

N = int(input())
q = Queue()

for _ in range(N):
    commend, *operand = input().split()
    node = [Node(*operand)] if operand else []
    q.action(commend, *node)
    
