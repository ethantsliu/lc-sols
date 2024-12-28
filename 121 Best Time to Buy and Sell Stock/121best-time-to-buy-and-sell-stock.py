class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        i = 0
        j = 1
        profit = 0
        while j < len(prices):
            diff = prices[j] - prices[i]
            if prices[j] > prices[i]:
                profit = diff if diff > profit else profit
            else:
                i = j
            j += 1
        
        return profit
