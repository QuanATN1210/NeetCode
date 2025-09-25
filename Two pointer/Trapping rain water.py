'''
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000
'''
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        prefix = [height[0]]*len(height)
        suffix = [height[len(height)-1]]*len(height)
        res = 0
        for i in range(1,len(height)):
            prefix[i] = max(prefix[i-1],height[i])
        for i in range(len(height) - 2,-1,-1):
            suffix[i] = max(suffix[i+1],height[i])
        for i in range(len(height)):
            res += min(prefix[i],suffix[i]) - height[i]
        return res
'''

'''