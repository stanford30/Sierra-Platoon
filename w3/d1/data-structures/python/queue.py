class Queue:
    # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        # write your code to add data to the Queue following FIFO and return the Queue
        self.queue.append(data)

    def dequeue(self):
        # write your code to removes the data to the Queue following FIFO and return the Queue
        self.queue.pop(0)

    def size(self):
        # write your code that returns the size of the Queue
        print(len(self.queue))


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.queue)
q.size()
q.dequeue()
print(q.queue)
