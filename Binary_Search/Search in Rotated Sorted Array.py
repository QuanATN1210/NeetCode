'''
Search in Rotated Sorted Array
Solved 
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l =0
        r = len(nums) -1
        mini = 0
        if r == 0:
            mini =0
        elif nums[r] > nums[l]:
            mini = l
        else:
            while l<r:
                mini = (l+r)//2
                
                if nums[mini] <= nums[r]:
                    r =mini 
                elif nums[mini] >nums[r]:
                    l = mini +1
            mini =l

        if target <= nums[-1]:
            
            l=mini
            r = len(nums)-1
            while l<=r:
                m = (l+r)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
        else:
            l=0
            r=mini-1
            while l<=r:
                m=(l+r)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l= m+1

        return -1
'''
Time complexity O(logn)
Space complexity O(1)
'''