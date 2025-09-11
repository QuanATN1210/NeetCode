'''
Longest Common Prefix
Solved 
You are given an array of strings strs. Return the longest common prefix of all the strings.

If there is no longest common prefix, return an empty string "".

Example 1:

Input: strs = ["bat","bag","bank","band"]

Output: "ba"
'''
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        result = ""
        mini = min(len(s) for s in strs)
        
        for i in range(mini):
            chu = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != chu:
                    return result
                else:
                    continue
            result += chu
        return result

'''
Time & Space Complexity
Time complexity: O(n*m)
Space complexity: O(1)
'''