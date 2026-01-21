from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("front from an empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def __str__(self):
        return "Queue(" + ", ".join(repr(item) for item in self.items) + ")"
    

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)         
    print(queue.dequeue())    
    print(queue.front())   
    print(queue.size())   
   
