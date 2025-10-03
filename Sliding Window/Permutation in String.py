'''
Permutation in String
Solved 
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count ={}
        for s in s1:
            count[s] = 1+ count.get(s,0)
        
        for i in range(len(s2)):
            copy_count = count.copy()
            j = i
            index = 0
            while j < len(s2) and index < len(s1):
                a = copy_count.get(s2[j],0)
                if a == 0:
                    break
                else:
                    copy_count[s2[j]] = a-1
                    index +=1
                    j+=1
            if index == len(s1):
                return True

        return False 
'''
Time complexity O(n*m)
Space complexity O(n*m)
'''