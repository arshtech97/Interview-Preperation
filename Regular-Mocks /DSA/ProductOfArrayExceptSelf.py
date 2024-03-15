# Problem Statement: https://leetcode.com/problems/product-of-array-except-self

class Solution:
    # T.C: O(N), S.C: O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n

        # left[i] = Multiplication of all the elements in this range [0 .. i-1]
        # right[i] = Multiplication of all the elements in this range [i+1 .. n-1]
        left[0] = 1
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        right[n-1] = 1
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        # after left and right are calculated multiply elements from both lists to get result
        result = [0] * n
        for i in range(n):
            result[i] = left[i] * right[i]
        
        return result