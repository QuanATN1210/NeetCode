'''
Top K Frequent Elements
Solved 
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
'''

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        freq =[[] for i in range(len(nums)+1)]
        for num in nums:
            count[num]=1+count.get(num,0)
        for key,value in count.items():
            freq[value].append(key)
        res =[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
'''
Time complexity O(n)
Space complexity O(n)
'''