class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_key = 0
        self.dict = {}

    def append(self, item):
        if self.current_key >= self.capacity - 1:
            self.current_key = 0
        else:
            self.current_key += 1
            
        self.dict[self.current_key] = item
            
    def get(self):
        return list(self.dict.values())