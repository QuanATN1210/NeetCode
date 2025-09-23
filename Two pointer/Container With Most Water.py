'''
You are given an integer array heights where heights[i] represents the height of the 
i
t
h
i 
th
  bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:



Input: height = [1,7,2,5,4,7,3,6]

Output: 36
'''
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        res = 0
        while i < j:
            current = min(heights[i],heights[j])*(j-i)
            res = max(current,res)
            if (heights[i]<heights[j]):
                i+=1
            else:
                j-=1
        return res
'''
Time complexity O(n)
Space complexity O(1)
'''