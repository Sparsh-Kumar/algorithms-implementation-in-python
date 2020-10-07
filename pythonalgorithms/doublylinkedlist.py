

class Node:

    def __init__ (self, prev = None, cargo = None, next = None):

        self.prev = prev
        self.cargo = cargo;
        self.next = next;

    def __del__ (self):
        pass;


class DoublyLL:

    def __init__ (self):
        self.__start = None;

    def insert (self, cargo = None):
        node = Node (None, cargo, None)
        if not self.__start:
            self.__start = node;
        else:
            startNode = self.__start;
            while startNode.next:
                startNode = startNode.next;
            node.prev = startNode;
            startNode.next = node;

    def display (self, startNode = None):

        if not startNode:
            startNode = self.__start;
        while startNode:
            print (startNode.cargo, startNode.prev, startNode, startNode.next)
            startNode = startNode.next;

    def __del__ (self):
        pass;


def main ():

    doublylinkedlist = DoublyLL ();
    for i in range (1, 4, 1):
        doublylinkedlist.insert (i)
    doublylinkedlist.display ()

if __name__ == '__main__':
    main ()