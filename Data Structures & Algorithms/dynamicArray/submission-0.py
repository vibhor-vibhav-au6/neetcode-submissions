class DynamicArray:
    
    def __init__(self, capacity: int):
        self.l = [None] * capacity
        self.capacity = capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.l[i]
        


    def set(self, i: int, n: int) -> None:
        self.l[i] = n
        return

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.l[self.size] = n
        self.size += 1
        return

    def popback(self) -> int:
        res = self.l[self.size - 1]
        self.size -= 1
        return res
 

    def resize(self) -> None:
        capacity = self.capacity
        self.l += [None]* capacity
        self.capacity = 2 * capacity
        return


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
