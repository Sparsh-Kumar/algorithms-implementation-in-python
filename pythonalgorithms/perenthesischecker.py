

class Node:
    def __init__ (self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next
    def __del__ (self):
        pass;

class Stack:
    def __init__ (self):
        self.top = None;
        self.stacklength = 0;
    def push (self, cargo = None):
        node = Node (cargo)
        if not self.top:
            self.top = node;
        else:
            startNode = self.top
            node.next = startNode
            self.top = node
        self.stacklength = self.stacklength + 1;
    def pop (self):
        item = None
        if self.top:
            item = self.top
            self.top = self.top.next
        self.stacklength = self.stacklength - 1;
        return item
    def display (self):
        startNode = self.top
        while startNode:
            print (startNode.cargo)
            startNode = startNode.next
    def __del__ (self):
        pass;

def CheckExpression (expression = None):
    if not expression:
        return False;
    stack = Stack ();
    for i in expression:
        if i == '(' or i == '[' or i == '{':
            stack.push (i)
        else:
            if i == ')':
                item = stack.pop ()
                if not item or item.cargo != '(':
                    return False
            elif i == ']':
                item = stack.pop ()
                if not item or item.cargo != '[':
                    return False
            elif i == '}':
                item = stack.pop ()
                if not item or item.cargo != '{':
                    return False
            else:
                continue;
    if stack.stacklength == 0:
        return True
    else:
        return False

def main ():
    expression = '{(A+B)*(C+D)';
    isvalid = CheckExpression (expression)
    if isvalid:
        print ('Correct Expression')
    else:
        print ('Incorrect Expression')

if __name__ == '__main__':
    main ()