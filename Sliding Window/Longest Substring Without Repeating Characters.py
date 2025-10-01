'''
Longest Substring Without Repeating Characters
Solved 
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 :
            return 0
        if len(s) == 1 :
            return 1
        char = set()
        l= 0
        r =1
        char.add(s[l])
        result = 1
        while r < len(s):
            if s[r] not in char:
                char.add(s[r])
                result = max(result,r-l+1)
            else:
                while s[r] in char:
                    char.remove(s[l])
                    l+=1
                char.add(s[r])
                
            r+=1
        return result
    
'''
Time complexity O(n)
Space complexity O(m)
'''