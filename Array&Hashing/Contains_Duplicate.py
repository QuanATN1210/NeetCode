'''
Contains Duplicate
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
'''
from typing import List, Tuple, Dict, Any
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mark = set()
        for num in nums:
            if num in mark:
                return True
            else:
                mark.add(num)
        return False   


'''
Time & Space Complexity
Time complexity: O(n)
Space complexity: O(n)
'''
