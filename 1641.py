class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1]*5
        for i in range(1,n):
            for j in range(1,5):
               result[j] = result[j]+result[j-1]
        return sum(result)       