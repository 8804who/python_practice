from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__dict = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.__dict:
            self.__dict.move_to_end(key)
            return self.__dict[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.__dict:  
            self.__dict.move_to_end(key)

        self.__dict[key] = value

        if len(self.__dict) > self.__capacity:
            self.__dict.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)