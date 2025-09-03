class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data!= key:
            prev = current
            current = current.next
        if not current:
            print(f"Value {key} not found in the list.")
            return
        prev.next = current.next
        current = None
    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes) + " -> None")
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
ll = LinkedList()
ll.append(15)
ll.append(30)
ll.prepend(5)
ll.display()  
print("Deleting 5...")
ll.delete(5)
ll.display() 
print("Searching for 30:", ll.search(30))  
print("Searching for 100:", ll.search(100))  