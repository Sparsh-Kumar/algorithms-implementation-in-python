
class Node:
    def __init__ (self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next
    def __del__ (self):
        pass;

class Stack:
    def __init__ (self):
        self.top = None;
        self.stacklength = 0
    def push (self, cargo = None):
        if cargo:
            node = Node (cargo)
            if not self.top:
                self.top = node;
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
            self.top = self.top.next;
        return item
    def __del__ (self):
        pass;

def evalprefix (prefixexp = None):
    if not prefixexp:
        return False;
    stack = Stack ()
    for i in range (len (prefixexp) - 1, -1, -1):
        if prefixexp [i].isdigit ():
            stack.push (int (prefixexp [i]))
        else:
            if prefixexp [i] == '+':
                i1 = stack.pop ()
                i2 = stack.pop ()
                if not i1 or not i2:
                    return False
                stack.push (i1.cargo  + i2.cargo)
            elif prefixexp [i] == '*':
                i1 = stack.pop ()
                i2 = stack.pop ()
                if not i1 or not i2:
                    return False;
                stack.push (i1.cargo * i2.cargo)
            elif prefixexp [i] == '/':
                i1 = stack.pop ()
                i2 = stack.pop ()
                if not i1 or not i2:
                    return False
                else:
                    stack.push (i1.cargo / i2.cargo)
            elif prefixexp [i] == '-':
                i1 = stack.pop ()
                i2 = stack.pop ()
                if not i1 or not i2:
                    return False;
                else:
                    stack.push (i1.cargo - i2.cargo)
            else:
                return False
    return stack.pop ().cargo
    
def main ():
    prefixexp = '*+23+45'
    result = evalprefix (prefixexp)
    if not result:
        print ('Error')
    else:
        print (result)

if __name__ == '__main__':
    main ()