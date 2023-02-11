class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack1 =[]
        i=0
        for num in pushed:
            stack1.append(num)
            print(num)
            while len(stack1)>0 and stack1[len(stack1)-1] == popped[i]:
                stack1.pop()
                i +=1
        return True if len(stack1) ==0 else False
        