from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        mydict = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            mydict[tuple(count)].append(s)
        
        return mydict.values()
