class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        min_val = float('inf')
        index = -1
        for i, v in enumerate(points):
           if v[0] == x or v[1] == y:
               distance = abs(x-v[0]) + abs(y-v[1])
               if distance < min_val:
                   min_val = distance
                   index = i
        return index


        

