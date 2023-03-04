class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        p=permutations(nums)
        result =[]
        print(p)
        print(nums)
        for i in p:
            if i not in result:
                result.append(i)
        return result