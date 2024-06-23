class Queue:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
    
    def is_empty(self):
        return True if len(self.data) == 0 else False
    
    def is_full(self):
        return True if len(self.data) == self.capacity else False
    
    def dequeue(self):
        return self.data.pop(0)
    
    def enqueue(self, item):
        return self.data.append(item)
    
    def front(self):
        return self.data[0]
    
#test
my_queue = Queue(capacity=5)
my_queue.enqueue(1)
my_queue.enqueue(2)
print(my_queue.is_full())
print(my_queue.front())
print(my_queue.dequeue())
print(my_queue.front())
print(my_queue.dequeue())
print(my_queue.is_empty())