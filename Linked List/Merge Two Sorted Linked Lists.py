'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        head = None
        tail = None
        i=0
        while cur1 and cur2:
            if i ==0:
                if cur1.val < cur2.val:
                    head = cur1
                    tail = head
                    cur1 = cur1.next
                else:
                    head = cur2
                    tail = head
                    cur2 = cur2.next
            else:
                if cur1.val < cur2.val:
                    tail.next = cur1
                    cur1 = cur1.next
                    tail = tail.next
                else:
                    tail.next = cur2
                    cur2 = cur2.next
                    tail = tail.next
            i+=1

        if i == 0:
            if cur1:
                return cur1
            elif cur2:
                return cur2
            else:
                return head
        
        while cur1:
            tail.next = cur1
            tail = tail.next
            cur1 = cur1.next
        
        while cur2:
            tail.next = cur2
            tail = tail.next
            cur2 = cur2.next
        
        return head

'''
Time complexity O(n+m)
Space complexity O(1)
'''