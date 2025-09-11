'''
Group Anagrams
Solved 
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
'''
from typing import List, Tuple, Dict, Any

class Solution:
    def isAnagrams(self,s: str, t: str)-> bool:
        if len(s) != len(t):
            return False
        countS={}
        countT={}
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0) 
        for i in range(len(s)):
            if countS[s[i]] != countT.get(s[i],0):
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        result =[]
        sub =[]
        i=1
        while len(strs)>0:
            if len(sub) == 0:
                sub = [strs[0]]
            if i<len(strs) and self.isAnagrams(strs[0],strs[i]):
                sub.append(strs[i])
            if i == len(strs) - 1:
                result.append(sub)
                strs = [x for x in strs if x not in sub]                
                sub =[]
                i=1
                continue
            if len(strs) == 1:
                result.append(sub)
                break

            i=i+1
        return result

'''
Time & Space Complexity
Time complexity: O(n*m^2)
Space complexity: O(n*m)
'''

        