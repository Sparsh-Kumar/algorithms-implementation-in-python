

class Node:
    def __init__ (self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next
    def __del__ (self):
        pass;


class Stack:
    def __init__ (self):
        self.top = None
        self.stacklength = 0
    def push (self, cargo = None):
        if cargo:
            node = Node (cargo)
            if not self.top:
                self.top = node;
            else:
                startNode = self.top
                node.next = startNode
                self.top = node
            self.stacklength = self.stacklength + 1;
    def pop (self):
        item = None;
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

def getpref (op):
    if op == '+' or op == '-':
        return 0;
    elif op == '*' or op == '/':
        return 1;
    else:
        return -1;

def infixtopostfix (expression = None):
    if not expression:
        return None
    expression = expression + ')'
    stack = Stack ();
    stack.push ('(');
    print (expression)
    result = ''
    for i in expression:
        if i == '(':
            stack.push (i)
        elif i == ')':
            while True:
                item = stack.pop ()
                if not item or item.cargo == '(':
                    break;
                else:
                    result = result + item.cargo
        elif i == '+' or i == '-' or i == '*' or i == '/':
            while True:
                item = stack.pop ();
                if not item or getpref (item.cargo) < getpref (i) or getpref (item.cargo) < 0:
                    if item:
                        stack.push (item.cargo)
                    break;
                else:
                    result = result + item.cargo
            stack.push (i)
        else:
            result = result + i
    return result

def main ():
    expression = '(A+B)*(C+D)';
    postfix = infixtopostfix (expression)
    if not postfix:
        print ('Not a valid expression')
    else:
        print (postfix)

if __name__ == '__main__':
    main ();
