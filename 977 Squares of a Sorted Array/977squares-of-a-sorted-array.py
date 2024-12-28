class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        if nums[0] > 0:
            return [num**2 for num in nums]
        if nums[-1] < 0:
            return [num**2 for num in nums[::-1]]

        #find the first positive index
        first_pos = 0
        for i, n in enumerate(nums):
            if n>=0:
                first_pos = i
                break

        pos, neg = nums[first_pos:], [-1*rev for rev in nums[:first_pos][::-1]]

        #merge the two 
        i = j = 0
        res = []
        while i < len(pos) and j < len(neg):
            if pos[i] > neg[j]:
                res.append(neg[j])
                j+=1
            else:
                res.append(pos[i])
                i+=1
        
        if i < len(pos):
            res.extend(pos[i:])

        else: 
            res.extend(neg[j:])
        
        return [n**2 for n in res]

