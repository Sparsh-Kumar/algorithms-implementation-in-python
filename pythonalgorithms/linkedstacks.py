

class Node:
    def __init__ (self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next
    def __del__ (self):
        pass;


class Stack:
    def __init__ (self):
        self.top = None
    def push (self, cargo = None):
        if cargo:
            node = Node (cargo)
            if not self.top:
                self.top = node;
            else:
                startNode = self.top
                node.next = startNode
                self.top = node
    def pop (self):
        item = None
        if self.top:
            item = self.top
            self.top = self.top.next
        return item
    def display (self):
        startNode = self.top;
        while startNode:
            print (startNode.cargo)
            startNode = startNode.next
    def __del__ (self):
        pass;


def main ():
    s = Stack ();
    for i in range (1, 5, 1):
        s.push (i)
    s.display ()

    print ('Popping value')
    item = s.pop ()
    print ('Popped item = ',item.cargo)
    item = s.pop ()
    print ('Popped item = ', item.cargo)

    s.display ()
    
if __name__ == '__main__':
    main ()