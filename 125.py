class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = (s.replace(' ','')).lower()
        s =''.join(char for char in s if char.isalnum())
        left =0
        right = len(s) -1
        while left<right:
            if s[left] !=s[right]:
                return False
            left = left+1
            right -=1
        return True
              
