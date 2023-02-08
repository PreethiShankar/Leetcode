class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        arr1, arr2, result = list(word1), list(word2),''
        while arr1 and arr2:
            result += arr1.pop(0) if arr1>=arr2 else arr2.pop(0)
        return result+''.join(arr1) +''.join(arr2)
            