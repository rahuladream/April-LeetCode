class Queue:
    def __init__(self):
        self.queue = list()
    
    def add_element(self, val):
        # Insert element
        if val not in self.queue:
            self.queue.insert(0, val)
            return True
        return False
    
    def size(self):
        # Size of queue
        return len(self.queue)

    def remove_element(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("Queue is empty")
    


the_queue = Queue()
the_queue.add_element('Apple')
the_queue.add_element('Mango')
print("The length of queue: {}".format(the_queue.size()))

print(the_queue.remove_element())