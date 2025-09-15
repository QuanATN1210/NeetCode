class ListNode:
    def __init__(self, key = -1, value = -1,next =None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.data =[ListNode() for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        cur = self.data[key%1000]
        if cur.key == -1:
            cur.key = key
            cur.value = value
            return
        if cur.key == key:
            cur.value = value
            return
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

    def get(self, key: int) -> int:
        cur = self.data[key%1000]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1
        
    def remove(self, key: int) -> None:
        cur = self.data[key%1000]
        if cur.key == key:
            if cur.next == None:
                cur.key =-1
                cur.value =-1
                return
            else:
                self.data[key%1000]=cur.next
                return
        while cur.next:
            if cur.next.key == key:
                cur.next == cur.next.next
                return
            cur =cur.next

        



                

            
    
'''
Time complexity O(n/k) n:number of key , k: size map
Space complexity O(k+m) m: number of unique key
'''