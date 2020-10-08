

import copy

class Node:
    def __init__ (self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next
    def __del__ (self):
        pass;


class LQueue:
    def __init__ (self):
        self.front, self.rear = None, None
    def insert (self, cargo= None):
        if cargo:
            node = Node (cargo)
            if not self.front or not self.rear:
                self.front, self.rear = node, node
            else:
                self.rear.next = node;
                self.rear = self.rear.next;
    def remove (self):
        item = None
        if self.front:
            item = self.front
            self.front = self.front.next
        return item
    def display (self):
        startNode = self.front
        while startNode != self.rear:
            print (startNode.cargo, startNode, startNode.next)
            startNode = startNode.next
        print (startNode.cargo, startNode, startNode.next)
    def __del__ (self):
        pass;

def main ():
    lq = LQueue ();
    for i in range (1, 4, 1):
        print ('Iteration = ',i)
        lq.insert (i)
        lq.display ()
    print ('Removing the Node');
    lq.remove ()
    lq.display ()
if __name__ == '__main__':
    main ()