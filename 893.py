class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        list1=[]
        
        for i in range(len(words)):
            eve =''
            odd =''
            for j in range(len(words[i])):
                if j%2==0:
                    eve +=words[i][j]
                else:
                    odd +=words[i][j]
                str = sorted(eve)+sorted(odd)
            list1.append(''.join(str))
        print(list1)
        return len(Counter(list1))

                

