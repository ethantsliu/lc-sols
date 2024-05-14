class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x
        while (l<=r):
            m = (r+l)//2
            if (m * m >x): r = m-1
            elif (m * m < x): l = m+1
            else: return m

        return r
        

