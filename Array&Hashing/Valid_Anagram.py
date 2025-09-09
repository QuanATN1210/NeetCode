'''
alid Anagram
Solved 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
'''
from typing import List, Tuple, Dict, Any
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS ={}
        countT ={}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        for i in range(len(s)):
            if countS[s[i]] != countT.get(s[i],0):
                return False
        return True

'''
Time & Space Complexity
Time complexity: O(n)
Space complexity: O(1) since we have at most 26 different charecters
'''