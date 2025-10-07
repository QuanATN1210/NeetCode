'''
ou are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
'''
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        size=0
        while node:
            node = node.next
            size+=1
        
        i=1
        remove = head
        prev = None
        while remove:
            if i == size - n +1:
                if i == 1:
                    head = head.next
                    remove.next = None
                    return head
                elif i == size:
                    prev.next = None
                    return head
                else:
                    prev.next = remove.next
                    remove.next = None
                    return head
            else:
                prev = remove
                remove = remove.next
                i+=1
    
'''
Time complexity O(n)
Space complexity O(1)
'''