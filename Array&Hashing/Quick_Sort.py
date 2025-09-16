from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, l, r):
            pivot = arr[r]
            i = l - 1
            for j in range(l, r):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            i += 1
            arr[i], arr[r] = arr[r], arr[i]  # Đổi chỗ pivot đúng vị trí
            return i

        def quickSort(arr, l, r):
            if l >= r:
                return
            p = partition(arr, l, r)
            quickSort(arr, l, p - 1)
            quickSort(arr, p + 1, r)

        quickSort(nums, 0, len(nums) - 1)
        return nums
    
'''
Time complexity O(n*logn) worst O(n^2)
Space complexity O(logn)
'''