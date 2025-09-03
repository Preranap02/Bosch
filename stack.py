class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def __str__(self):
        return "Stack(bottom -> top): " + str(self.items)

stack = Stack()

stack.push(30)
stack.push(60)
stack.push(90)
print(stack)  

print("Top element is:", stack.peek())

print("Popped:", stack.pop())
print("Popped:", stack.pop())

print(stack)
print("Is stack empty?", stack.is_empty())

print("Popped:", stack.pop())

print("Is stack empty?", stack.is_empty())

try:
        stack.pop()
except IndexError as e:
        print("Error:", e)