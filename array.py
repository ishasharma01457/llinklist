from multiprocessing.sharedctypes import Value


class Queuearray:
 
   
    def __init__(self, size=100):
        self.q = [None] * size      
        self.capacity = size        
        self.front = 0              
        self.rear = -1              
        self.count = 0              
 
    
    def dequeue(self):
        
        if self.isEmpty():
            print(' Underflow')
            exit(-1)
        Value = self.q[self.front]
        print('delete', Value)
        self.front = (self.front + 1) % self.capacity
        self.count = self.count - 1
        return Value
 
    
    def enqueue(self, data):
       
        if self.isFull():
            print('Overflow')
            exit(-1)
        print('Insertion', data)
        self.rear = (self.rear + 1) % self.capacity
        self.q[self.rear] = data
        self.count = self.count + 1
 
    def peek(self):
        if self.isEmpty():
            print(' UnderFlow')
            exit(-1)
        return self.q[self.front]
 
    
    def size(self):
        return self.count
 
   
    def isEmpty(self):
        return self.size() == 0
 
   
    def isFull(self):
        return self.size() == self.capacity
 
 
if __name__ == '__main__':
 
    q = Queuearray(5)
 
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
 
    print(' size is', q.size())
    print('The  top element is', q.peek())
    q.dequeue()
    print('The top element is', q.peek())
 
    q.dequeue()
    q.dequeue()
 
    if q.isEmpty():
        print('null')
    else:
        print('elements')
