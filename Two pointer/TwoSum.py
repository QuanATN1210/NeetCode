'''
Two Integer Sum II
Solved 
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O
(
1
)
O(1) additional space.

Example 1:

Input: numbers = [1,2,3,4], target = 3

Output: [1,2]
'''
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i =0
        j = len(numbers) -1
        res =[]
        while i<j:
            if numbers[i] + numbers[j] == target:
                res.append(i+1)
                res.append(j+1)
                return res
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                j-=1
        return []
'''
Time complexity O(n)
Space complexity O(1)
'''