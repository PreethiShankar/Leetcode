class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr1= list(s)
        for i in range(len(arr1)):
            if arr1[i] =='?':
                for char in 'abc':
                    if (i==0 or arr1[i-1] != char) and (i+1==len(arr1) or arr1[i+1] !=char):
                        arr1[i] = char
                        break
        return ''.join(arr1)
