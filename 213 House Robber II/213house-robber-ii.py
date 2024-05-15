class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1, rob2 = 0, 0

        if len(nums) == 1: return nums[0]

        for n in nums[1:]:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        
        rrob1, rrob2 = 0, 0
        
        for n in nums[:-1]: 
            temp = max(rrob1 + n, rrob2)
            rrob1 = rrob2
            rrob2 = temp
        
        return max(rrob2, rob2)