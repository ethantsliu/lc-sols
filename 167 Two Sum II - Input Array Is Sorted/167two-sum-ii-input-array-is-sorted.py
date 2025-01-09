class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        add = numbers[i]+numbers[j]
        while add != target:
            if add < target:
                i+=1
            elif add > target:
                j-=1  
            add = numbers[i] + numbers[j]  
        return [i+1, j+1]