'''
Valid Palindrome

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
'''
from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
         i = 0
         j = len(s) -1
         
         while i<j:
            if s[i].isalnum() is False:
                i+=1
                continue
            if s[j].isalnum() is False:
                j-=1
                continue 
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
                
         return True
     
'''
Time comlexity O(n)
Space complexity O(1)
'''