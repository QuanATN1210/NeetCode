'''
Top K Frequent Elements
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
        for num in nums:
            count[num]=1+count.get(num,0)
        arr =[]
        for key,value in count.items():
            arr.append([value,key])
        arr.sort()
        res =[]
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        

        

'''
Time complexity O(nlog(n))
Space complexity O(n)
'''