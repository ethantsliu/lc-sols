class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mul = 1
        output = []

        for i in nums: 
            output.append(mul)
            mul *= i
                
        mul = 1 # reset mul
        print(output)

        # Iterate backwards
        for i in range(len(nums)-1, -1, -1):
            output[i] = mul * output[i]
            mul *= nums[i]
        
        return output