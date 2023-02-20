class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
       
        # s = list(s)
        i = len(nums) -2
     
        while i>=0 and nums[i+1]<=nums[i]:
            i = i-1
        if i>=0:
            j = len(nums)-1
            while nums[j]<=nums[i]:
                j= j-1
            nums[i], nums[j] = nums[j], nums[i]
        nums[:] = nums[:i+1]+nums[i+1:][::-1]

