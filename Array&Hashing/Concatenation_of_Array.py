'''
You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:

Input: nums = [1,4,1,2]

Output: [1,4,1,2,1,4,1,2]
'''
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result =[]
        for i in range(2*n):
            if i < n:
                result.append(nums[i])
            else:
                result.append(nums[i-n])
        return result  
    
    
'''
Time & Space Complexity
Time complexity: O(n)
Space complexity: O(n)
'''