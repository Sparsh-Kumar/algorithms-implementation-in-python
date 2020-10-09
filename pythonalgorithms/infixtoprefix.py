

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
                self.top = node
            else:
                startNode = self.top
                node.next = startNode
                self.top = node;
            self.stacklength = self.stacklength + 1;
    def pop (self):
        item = None
        if self.top:
            item = self.top
            self.stacklength = self.stacklength - 1;
            self.top = self.top.next
        return item
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
        return False;
    stack = Stack ()
    postfix = ''
    stack.push ('(')
    expression = expression + ')'
    for i in expression:
        if i == '(':
            stack.push ('(')
        elif i == ')':
            while True:
                item = stack.pop ()
                if not item or item.cargo == '(':
                    break;
                else:
                    postfix = postfix + item.cargo
        elif i == '+' or i == '-' or i == '*' or i == '/':
            while True:
                item = stack.pop ()
                if not item or getpref (item.cargo) < getpref (i) or getpref (item.cargo) < 0:
                    if item:
                        stack.push (item.cargo)
                    break;
                else:
                    postfix = postfix + item.cargo
            stack.push (i)
        else:
            postfix = postfix + i
    return postfix

def infixtoprefix (expression = None):
    if not expression:
        return False
    newexpression  = ''
    for i in range (len (expression) - 1, -1, -1):
        if expression [i] == ')':
            newexpression = newexpression + '('
        elif expression [i] == '(':
            newexpression = newexpression + ')'
        else:
            newexpression = newexpression + expression [i]
    result = infixtopostfix (newexpression)
    if not result:
        return False
    return result [::-1]

def main ():
    expression = '(A+B)*(C+D)'
    prefix = infixtoprefix (expression)
    if not prefix:
        print ('Expression is not correct')
    else:
        print (prefix)

if __name__ == '__main__':
    main ()