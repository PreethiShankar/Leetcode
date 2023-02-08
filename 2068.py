class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        from collections import Counter
        cnt1 = Counter(word1)
        
        for ch in word2:
            cnt1[ch] = cnt1[ch]-1
        return max(abs(val) for val in cnt1.values())<=3