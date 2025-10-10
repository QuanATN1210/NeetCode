'''
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        bonus = 0
        head,cur = None, None
        while l1 and l2:
            val = l1.val + l2.val + bonus
            if val >=10:
                if bonus == 0:
                    bonus = 1
                val = val - 10
            else:
                if bonus == 1:
                    bonus = 0

            
            if head == None:
                head = ListNode(val=val)
                cur= head
            else:
                cur.next = ListNode(val=val)
                cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        if l1 is None and l2 is None:
            if bonus == 1:
                cur.next = ListNode(val=1)
        elif l2 is None:
            while l1:
                val = l1.val + bonus
                if val >=10:
                    if bonus == 0:
                        bonus =1
                    val = val - 10
                else:
                    if bonus == 1:
                        bonus = 0
                cur.next = ListNode(val=val)
                cur = cur.next
                l1 = l1.next
            if bonus ==1 :
                cur.next = ListNode(val=1)
        elif l1 is None:
            while l2:
                val = l2.val + bonus
                if val >=10:
                    if bonus == 0:
                        bonus =1
                    val = val - 10
                else:
                    if bonus == 1:
                        bonus = 0
                cur.next = ListNode(val=val)
                cur = cur.next
                l2 = l2.next
            if bonus ==1 :
                cur.next = ListNode(val=1)
        
        return head

            




        