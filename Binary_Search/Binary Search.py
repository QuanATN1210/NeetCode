'''
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O(logn)
O(logn) time.
'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        m = (r+l)//2
        while l <= r:
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
                m = (l+r)//2
            else:
                r =m - 1
                m = (l+r)//2
        return -1

'''
Time complexity O(log(n))
Space complexity O(1)
'''