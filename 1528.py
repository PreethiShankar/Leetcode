class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        output=[None] *len(indices)
        for i in range(len(indices)):
            output[indices[i]] = s[i]
        return ''.join(output)
