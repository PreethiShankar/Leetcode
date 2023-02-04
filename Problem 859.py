from collections import Counter
class Solution(object):
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False
        CountS= Counter(s)
        Countgoal= Counter(goal)
        if CountS != Countgoal:
            return False
        diff = sum([i!=j for i, j in zip(s, goal)])
        if diff not in [0,2]:
            return False
        if diff ==0 and len(CountS) == len(s): False #All characters are different
        if diff ==2 and len(CountS) == 1: False #All characters are same
        return True
        
        
