class Heap:
    def __init__(self):
        self.heap = list()
    
    def insert(self,x):
        self.heap.append(x)
        i = len(self.heap) - 1
        while((i > 0) and (self.heap[i] < self.heap[i//2])):
            self.heap[i//2],self.heap[i] = self.heap[i],self.heap[i//2]
            i = i//2

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap[0]
        min = self.heap[0]
        self.heap[0] = self.heap.pop(len(self.heap)-1)
        i = 0
        while(self.heap[i] > self.heap[2*i + 1] or self.heap[i] > self.heap[2*i + 2]):
            if(self.heap[i] > self.heap[2*i + 1]):
                self.heap[i],self.heap[2*i + 1] = self.heap[2*i + 1],self.heap[i]
                i = 2*i + 1
            else:
                self.heap[i],self.heap[2*i + 2] = self.heap[2*i + 2],self.heap[i]
                i = 2*i + 2
        return min



if __name__=="__main__":
    h =  Heap()
    h.insert(1)
    h.insert(2)
    h.insert(3)
    h.insert(4)
    h.insert(5)
    h.insert(6)
    h.insert(7)
    h.insert(8)
    h.insert(9)
    h.insert(-1)
    h.insert(-2)
    h.insert(-1)
    h.insert(-2)




    print(h.heap)
    print(h.extract_min())
    print(h.heap)
