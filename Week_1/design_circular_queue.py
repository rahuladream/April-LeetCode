class MyCircularQueue:

    def __init__(self, k: int):
        self.maxsize = k
        self.size = 0
        self.front = -1
        self.back = -1
        self.arr = [-1] * k

    def enQueue(self, value: int) -> bool:
        #move back pointer forward and add new value there
        if self.size == self.maxsize:
            return False
        if self.size == 0:
            #empty array so we will append element to index 0
            self.back = 0
            self.front = 0
        else:
            self.back += 1
            if self.back == self.maxsize:
                #if we past the end then loop back to front
                self.back = 0
        self.arr[self.back] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        #move the front pointer forward so we no longer use that previous value
        if self.size == 0:
            return False
        self.front += 1
        if self.front == self.maxsize:
            self.front = 0
        self.size -= 1
        if self.size == 0:
            self.front = -1
            self.back = -1
        return True

    def Front(self) -> int:
        return -1 if self.size == 0 else self.arr[self.front]

    def Rear(self) -> int:
        return -1 if self.size == 0 else self.arr[self.back]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxsize
