'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 

O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
'''
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix =[1]*len(nums)
        suffix =[1]*len(nums)
        res =[1]*len(nums)
        for i in range(1,len(nums)):
            prefix[i]= prefix[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]
        for i in range(len(nums)):
            res[i]=prefix[i]*suffix[i]
        return res
'''
Time complexity O(n)
Space complexity O(n)
'''