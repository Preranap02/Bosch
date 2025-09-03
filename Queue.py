class Queue:
    def __init__(self):
        self.items = []
    
    def addtoqueue(self, item):
        self.items.append(item)
        print(f"Added to queue: {item}")
    
    def removefromqueue(self):
        if self.is_empty():
            raise IndexError("Remove from empty queue")
        removed_item = self.items.pop(0)
        print(f"removed: {removed_item}")
        return removed_item
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

q = Queue()
q.addtoqueue(10)
q.addtoqueue(20)
q.addtoqueue(30)
q.addtoqueue(40)
print(f"Queue size: {q.size()}")
    
first = q.removefromqueue()  
print(f"First element removed: {first}")
    
print(f"New front element: {q.peek()}")
print(f"Queue size after one remove: {q.size()}")