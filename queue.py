class Queue():
    def __init__(self,size=5):
        self.size = size
        self._queue= [None]*size
        self.front = 0
        self.rear = 0

    def enqueue(self,value):
        if not self.isFull():
            self._queue[self.rear] = value
            self.rear = (self.rear + 1) % self.size 

    def dequeue(self):
        if not self.isEmpty():
            front = self.front
            self.front = (self.front + 1) % self.size
            return front   
    
    def isEmpty(self):
        return self.rear - self.front == 0 

    def isFull(self):
        return self.rear - self.front == -1 or self.rear - self.front == self.size-1

    def __str__(self):
        return str(self._queue)
        

def __test__():
    a = Queue()
    a.enqueue(3)
    a.enqueue(4)
    a.enqueue(5)
    a.enqueue(6)
    a.enqueue(4)
    print(a)

if __name__ == '__main__':
    __test__()

