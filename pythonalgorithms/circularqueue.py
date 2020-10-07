

front, rear = -1, -1
MAX_LENGTH = 5
queue = [None] * MAX_LENGTH

# In Queue insertion takes place at the rear end and removal takes place at the front end

def insert (cargo = None):
    global front, rear, MAX_LENGTH, queue
    if not cargo:
        return -1;
    else:
        # The first insertion condition
        if front == -1 or rear == -1:
            front, rear = front + 1, rear + 1

        # If the Queue is full or Overflow Condition
        elif front == 0 and rear == MAX_LENGTH - 1:
            return -1;

        # If the Queue has some space left in the beginning
        elif front != 0 and rear == MAX_LENGTH - 1:
            rear = 0

        # Otherwise increment the rear pointer
        else:
            rear = rear + 1;
        
        queue [rear] = cargo

def remove ():
    global front, rear, MAX_LENGTH, queue

    # If the Queue has underflow condition
    if front == -1 or rear == -1:
        return -1;
    
    #Getting the item first
    item = queue [front]

    #Setting the Queue front to None
    queue [front] = None

    # When repeated deletion lead to condition in which front == rear
    if front == rear:
        front, rear = -1, -1

    # When repeated deletion leads to the condition in which front == MAX_LENGTH -1 
    elif front == MAX_LENGTH - 1:
        front = 0
        
    # Increment the front pointer so that it points to the next
    else:
        front = front + 1;
    return item

def display ():
    for i in queue:
        print (i)

def main ():

    print ('Insertion taking place')
    for i in range (1, 6, 1):
        print ('Iteration = ', i)
        insert (i)
        display ()

    print ('Deletion taking place')
    for i in range (1, 6, 1):
        print ('Iteration = ',i)
        remove ()
        display ()

    #print ('front = ',front, 'rear = ',rear)
    insert (45);
    display ();
    
if __name__ == '__main__':
    main()