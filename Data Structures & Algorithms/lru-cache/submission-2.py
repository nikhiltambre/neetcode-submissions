class LRUCache:
    def __init__(self, capacity: int):
        self.cache=OrderedDict()
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key]=value
        self.cache.move_to_end(key)
        current_size=len(self.cache)
        if current_size>self.capacity:
           self.cache.popitem(last=False)
        
       
