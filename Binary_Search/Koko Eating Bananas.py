'''
Koko Eating Bananas
Solved 
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:

Input: piles = [1,4,3,2], h = 9

Output: 2
Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1, you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.

Example 2:

Input: piles = [25,10,23,4], h = 4

Output: 25
'''
from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        total_banana = sum(piles)
        min_k = result = math.ceil(total_banana/h)
        res = max_k
        #min_k =1
        while min_k <= max_k:
            time = 0
            mid_k = (max_k+min_k)//2
            for num in piles:
                time+= math.ceil(num/mid_k)
            
            if time > h:
                min_k = mid_k + 1
            else:
                res = mid_k
                max_k = mid_k-1
        
        return res

'''
Time complexity O(n*log(m))
Space complexity O(1)
'''





        

        

        