

class Node:

    def __init__ (self, prev = None, cargo = None, next = None):

        self.prev = prev;
        self.cargo = cargo;
        self.next = next;

    def __del__ (self):
        pass;


class DoublyCircularLL:

    def __init__ (self):
        self.__start = None;

    def insert (self, cargo = None):
        node = Node (None, cargo, None)
        if not self.__start:
            self.__start = node;
            node.prev = self.__start;
            node.next = self.__start;
        else:
            startNode = self.__start;
            while startNode.next != self.__start:
                startNode = startNode.next;
            node.prev = startNode;
            node.next = self.__start;
            startNode.next = node;
            self.__start.prev = node;

    def display (self, startNode = None):
        if not startNode:
            startNode = self.__start
        while startNode.next != self.__start:
            print (startNode.cargo, startNode.prev, startNode, startNode.next)
            startNode = startNode.next;
        print (startNode.cargo, startNode.prev, startNode, startNode.next)

    def __del__ (self):
        pass;

def main ():

    doublyCircularlinkedlist = DoublyCircularLL ();
    for i in range (1, 5, 1):
        doublyCircularlinkedlist.insert (i);
    doublyCircularlinkedlist.display ();

if __name__ == '__main__':
    main ()