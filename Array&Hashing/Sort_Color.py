'''
You are given an array nums consisting of n elements where each element is an integer representing a color:

0 represents red
1 represents white
2 represents blue
Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

You must not use any built-in sorting functions to solve this problem.

Example 1:

Input: nums = [1,0,1,2]

Output: [0,1,1,2]
Example 2:

Input: nums = [2,1,0]

Output: [0,1,2]
Constraints:

1 <= nums.length <= 300.
0 <= nums[i] <= 2.
Follow up: Could you come up with a one-pass algorithm using only constant extra space?
'''
from  typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        l,r = 0, len(nums) -1
        i=0
        while i<=r:
            if nums[i] == 0:
                nums[i],nums[l] = nums[l],nums[i]
                l+=1
            elif nums[i] ==2:
                nums[i],nums[r] = nums[r],nums[i]
                r-=1
                i-=1
            i+=1
        
'''
Using Three Pointer
Time complexity O(n)
Space complexity O(1)
'''