class MyHashSet:

    def __init__(self):
        self.data =[]

    def add(self, key: int) -> None:
        if key not in self.data:
            self.data.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.data
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
'''
Time complexity O(n) for each function call
Space complexity O(1)

'''

class MyHashSet:

    def __init__(self):
        self.data =[0]*31251

    def add(self, key: int) -> None:
        self.data[key//32] |= self.getMask(key)
        

    def remove(self, key: int) -> None:

        if self.contains(key):
            self.data[key//32] ^=self.getMask(key)

    def contains(self, key: int) -> bool:
        return  self.data[key//32] & self.getMask(key) != 0
        

    def getMask(self, key: int)->int:
        return 1 << (key%32)


'''
Time complexity O(1)
Space complexity O(k)  k = max_size/32 +1
'''
