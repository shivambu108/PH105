class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element
    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):  
            print("Circular Queue is full\n") 
        elif (self.head == -1):  
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else: 
            self.tail = (self.tail + 1) % self.k 
            self.queue[self.tail] = data 

    # Delete an element
    def dequeue(self):
        if (self.head == -1): 
            print("Circular Queue is empty\n") 
        elif (self.head == self.tail):  
            temp=self.queue[self.head] 
            self.head = -1
            self.tail = -1
            return temp
        else: 
            temp = self.queue[self.head] 
            self.head = (self.head + 1) % self.k 
            return temp

    def display(self): 
        if(self.head == -1): 
            print("No element in the Circular Queue") 
        elif (self.tail >= self.head): 
            for i in range(self.head, self.tail + 1): 
                print(self.queue[i], end=" ") 
        else: 
            for i in range(self.head, self.k): 
                print(self.queue[i], end=" ") 
            for i in range(0, self.tail + 1): 
                print(self.queue[i], end=" ") 
        print()

# Create a new circular queue
cq = CircularQueue(5)

# Insert 5 elements
for i in range(1, 6):
    cq.enqueue(i)
cq.display()  # Display the queue

# Delete 2 elements
cq.dequeue()
cq.dequeue()
cq.display()  # Display the queue

# Insert 2 elements
cq.enqueue(6)
cq.enqueue(7)
cq.display()  # Display the queue
