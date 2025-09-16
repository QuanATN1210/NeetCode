from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,l,m,r):
            left = arr[l:m+1]
            right = arr[m+1:r+1]
            i,j,k = l,0,0
            while j<len(left) and k<len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    i = i+1
                    j = j+1
                else:
                    arr[i] = right[k]
                    i = i +1
                    k =k+1
            while j<len(left):
                arr[i] = left[j]
                i = i+1
                j = j+1
            while k<len(right):
                arr[i] = right[k]
                i = i+1
                k = k+1

        def mergeSort(arr,l,r):
            if l==r:
                return
            m = (l+r)//2
            mergeSort(arr,l,m)
            mergeSort(arr,m+1,r)
            merge(arr,l,m,r)
        mergeSort(nums,0,len(nums)-1)
        return nums

'''
Time complexity O(n*log(n))
Space complexity O(n)
'''


        


        