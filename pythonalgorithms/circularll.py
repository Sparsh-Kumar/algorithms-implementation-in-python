

class Node:

    def __init__ (self, cargo = None, next = None):
        self.cargo = cargo;
        self.next = next;

    def __del__ (self):
        pass;


class CircularLL:

    def __init__ (self):
        self.__start = None;

    def insert (self, cargo = None):

        if cargo:
            node = Node (cargo);
            if not self.__start:
                self.__start = node;
            else:
                start = self.__start
                while start.next != self.__start:
                    start = start.next;
                start.next = node;
            node.next = self.__start;

    def display (self, startNode = None):
        
        if not startNode:
            startNode = self.__start
        while startNode.next != self.__start:
            print (startNode.cargo, startNode, startNode.next)
            startNode = startNode.next
        print (startNode.cargo, startNode, startNode.next)

    def __del__ (self):
        pass;


def main ():

    linkedList = CircularLL ();
    for i in range (1, 6, 1):
        linkedList.insert (i)
    linkedList.display ()

if __name__ == '__main__':
    main ()