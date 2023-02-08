class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        for i in range(len(s)):
            ans = s[i:] +s[:i]
            if ans == goal:
                return True
        return False