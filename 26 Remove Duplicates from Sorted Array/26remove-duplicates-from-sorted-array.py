class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        check = []
        i = 0

        while i < len(nums):
            if nums[i] not in check:
                check.append(nums[i])
            i+=1
        
        nums[:] = check

        return i