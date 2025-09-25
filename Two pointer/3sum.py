'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
'''
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if nums[i] == nums[i-1] and i >0:
                continue
            target = 0 - nums[i]
            j = i+1
            k = len(nums) - 1
            while j <k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i],nums[j],nums[k]])
                    old_value = nums[j]
                    j+=1
                    k-=1
                    while nums[j] == old_value and j < k:
                        j+=1
                elif nums[j] + nums[k] < target:
                    j+=1
                else:
                    k-=1
                 
        return res
'''
Time complexity O(n^2)
Space complexity O(1)
'''