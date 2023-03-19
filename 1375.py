class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        ans =0
        fsum =0
        isum=0
        for i, flip in enumerate(flips):
            fsum = fsum + flip
            isum = isum +i+1
            ans += (fsum ==isum)
        
        return ans


