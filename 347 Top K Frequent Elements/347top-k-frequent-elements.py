from heapq import heappop, heappush, heapify
class Solution:
    def topKFrequent(self, nums, k):
        mydict = {}
        for n in nums:
            mydict[n] = 1 + mydict.get(n, 0)

        min_heap = []
        for num, freq in mydict.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []
        while min_heap: result.append(heapq.heappop(min_heap)[1])

        return result[::-1]
        
        # mydict = {}
        # freq = [[] for i in range(len(nums) + 1)] 

        # for n in nums:
        #     mydict[n] = 1 + mydict.get(n, 0)

        # for n, c in mydict.items():
        #     freq[c].append(n)
        
        # res = []
        # for i in range(len(freq-1), 0, -1):
        #     for n in freq[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res