class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []
      
    def enqueue(self, item):
        self.item = item
        # insert (enqueue) item at back (index -1)
        self.storage.append(self.item)
        self.size += 1
    
    def dequeue(self):
        # remove (deque) element at front (index 0)
        if self.size == 0:
            return None
        else:
            remove = self.storage.pop(0)
            self.size -= 1
            return remove

    def leng(self):
        return self.size

        
