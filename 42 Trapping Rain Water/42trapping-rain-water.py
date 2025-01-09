class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        area = 0
        l = 0
        r = len(height) - 1
        left_max = height[0]
        right_max = height[-1]

        while l < r:
            if left_max < right_max:
                l+=1
                left_max = max(left_max, height[l])
                area += left_max - height[l]
            else:
                r-=1
                right_max = max(right_max, height[r])   
                area += right_max - height[r]         

        return area