class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        if len(s1)!=len(s2) or (s1.count('x') +s2.count('x'))%2 !=0 or (s1.count('y')+s2.count('y'))%2 !=0:
            return -1
        count =0
        s=''
        for i in range(len(s1)):
            if s1[i]!= s2[i]:
                s += s1[i]
        count = s.count('x')//2 +s.count('y')//2
     
        if s.count('x')%2 !=0 or s.count('y')%2 !=0:
                count = count+2
        return count
               
           
