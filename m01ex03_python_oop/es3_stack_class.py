class Stack():
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity

    def is_empty(self):
        return True if len(self.data) == 0 else False
    
    def is_full(self):
        return True if len(self.data) == self.capacity else False
    
    def pop(self):
        return self.data.pop(-1)
    
    def push(self, item):
        return self.data.append(item)
    
    def top(self):
        return self.data[-1]

#test    
my_stack = Stack(capacity=5)
my_stack.push(1)
my_stack.push(2)
print(my_stack.is_full())
print(my_stack.top())
print(my_stack.pop())
print(my_stack.top())
print(my_stack.pop())
print(my_stack.is_empty())