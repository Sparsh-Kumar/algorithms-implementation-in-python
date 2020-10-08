

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
            node = Node (cargo);
            if not self.top:
                self.top = node
            else:
                startNode = self.top;
                node.next = startNode
                self.top = node;
    def pop (self):
        item = None;
        if self.top:
            item = self.top
            self.top = self.top.next;
        return item
    def __del__ (self):
        pass;

def evaluatePostfix (expression = None):
    if not expression:
        return None
    stack = Stack ()
    for i in expression:
        if i.isdigit ():
            stack.push (int (i))
        else:
            m = stack.pop ()
            n = stack.pop ()
            if not m or not n:
                return None
            else:
                if i == '+':
                    stack.push (m.cargo + n.cargo)
                elif i == '-':
                    stack.push (m.cargo - n.cargo)
                elif i == '*':
                    stack.push (m.cargo * n.cargo)
                elif i == '/':
                    stack.push (m.cargo / n.cargo)
                else:
                    return None;
    return stack.pop ().cargo

def main ():
    expression = '23+4+5+';
    result = evaluatePostfix (expression)
    if not result:
        print ('Error not a valid expression')
    else:
        print (result)

if __name__ == '__main__':
    main ()