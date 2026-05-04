from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__dic = dict()
        self.__recent_hist = dict()
        self.__key_set = set()
        self.__q = deque()
        self.__turn = 0

    def get(self, key: int) -> int:
        self.__turn += 1
        
        if key in self.__dic:
            self.__recent_hist[key] = self.__turn
            self.__q.append([key, self.__turn])
            return self.__dic[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:        
        self.__turn += 1
        self.__dic[key] = value
        self.__q.append([key, self.__turn])
        
        if key not in self.__recent_hist:
            self.__recent_hist[key] = 0
        self.__recent_hist[key] = self.__turn
        self.__key_set.add(key)

        if len(self.__key_set) > self.__capacity:
            while self.__q:
                k, t = self.__q.popleft()

                if self.__recent_hist[k] == t:
                    self.__key_set.remove(k)
                    del self.__dic[k]
                    break

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)