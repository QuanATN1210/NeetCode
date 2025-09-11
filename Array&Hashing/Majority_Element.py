'''
Majority Element
Solved 
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [5,5,1,1,1,5,5]

Output: 5
Example 2:

Input: nums = [2,2,2]

Output: 2
'''
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countS ={}
        for i in range(len(nums)):
            countS[nums[i]] = 1+ countS.get(nums[i],0)
            if countS[nums[i]] > len(nums)/2:
                return nums[i]
'''
Time & Space Complexity
Time complexity: O(n)
Space complexity: O(n) 
'''



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = res =0
        for num in nums:
            if count == 0:
                res = num
            count +=(1 if num == res else -1)
        return res
'''
Time & Space Complexity
Time complexity: O(n)
Space complexity: O(1) 
'''