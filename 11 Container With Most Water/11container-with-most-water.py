class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #idea is to grab the two bars that are the tallest and furthest from each other
        i = 0 
        j = len(height)-1
        area = 0
        while i < j:
            if height[i] < height[j]:
                mini = height[i]
            else:
                mini = height[j]
            area = max((j-i) * mini, area)
            if mini == height[j]:
                j-=1
            else:
                i+=1
        return area