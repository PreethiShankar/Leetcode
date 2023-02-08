from collections import Counter
class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
       
        nwords = len(words)
        output =''.join(words)
        cnt1 = Counter(output)
        for val in cnt1.values():
            print(val)
            if val%nwords !=0:
              return False
        return True