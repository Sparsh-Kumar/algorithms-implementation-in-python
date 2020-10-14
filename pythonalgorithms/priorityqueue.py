
import random

class Node:
    def __init__ (self, cargo = None, priority = 0, next = None):
        self.cargo = cargo;
        self.priority = priority;
        self.next = next;
    def __del__ (self):
        pass;


class PriorityQueue:
    def __init__ (self):
        self.front, self.rear = None, None
        self.queuelength = 0;
    def insert (self, cargo = None, priority = 0):
        if cargo:
            node = Node (cargo, priority)
            if not self.front or self.front.priority >= node.priority:
                node.next = self.front;
                self.front = node;
            else:
                startNode = self.front;
                while startNode.next and startNode.next.priority <= node.priority:
                    startNode = startNode.next;
                node.next = startNode.next;
                startNode.next = node;
            self.queuelength = self.queuelength + 1;
    def remove (self):
        item = None
        if self.front:
            item = self.front
            self.front = self.front.next;
            self.queuelength = self.queuelength - 1;
        return item
    def display (self):
        startNode = self.front
        print ('Queue length is ',self.queuelength);
        while startNode:
            print ('Cargo = ',startNode.cargo,' Priority = ',startNode.priority);
            startNode = startNode.next;
    def __del__ (self):
        pass;

def generateRandomPriority (max, min):
    return random.randint(max, min)

def main ():
    pq = PriorityQueue ();
    data = [123, 35, 5, 6, 672, 345];
    for i in data:
        pq.insert (i, generateRandomPriority (-5, 5));
    pq.display ()

    print ('Popping the value from the Queue')
    item = pq.remove ();
    print ('Removed item Cargo = ',item.cargo,' Priority = ',item.priority);

    print ('Displaying again');
    pq.display ();

    pq.insert (13, -7);
    pq.display ();
if __name__ == '__main__':
    main ()