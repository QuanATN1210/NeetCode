'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.
'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit = 0
        l= 0
        r=1
        while r < len(prices):
            temp = prices[r] -prices[l]
            if temp >0:
                profit = max(temp,profit)
                r+=1
            else :
                l = r
                r+=1
        return profit

'''
Time complexity O(n)
Space complexity O(1)
'''