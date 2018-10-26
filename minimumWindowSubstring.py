#!/usr/bin/env python
# This needs Python 3.x
from sortArrayByParity import solution


class Solution:

    def isValid(self, o, t):
        valid = 0
        for i in o.keys():
            if i in t and t[i] >= o[i]:
                valid = 1
            else:
                return 0
        return valid
    
    
    
    
    def minWindow(self, s, t):
        if not t or not s:
            return ''
        
        tdict = {}
        odict = {}
        for i in t:
            odict[i] = odict.get(i, 0) + 1
            
        l, r = 0, 0
        result = ''
        lens = len(s)
        
        sublen = lens
        
        while r < lens:
            endchar = s[r]
            if endchar in odict:
                tdict[endchar] = tdict.get(endchar, 0) + 1
                
            while self.isValid(odict, tdict):
                if r - l < sublen:
                    sublen = r -l
                    result = s[l:r+1]
                
                startchar = s[l]
                if startchar in tdict:
                    tdict[startchar] -= 1
                l += 1
            r += 1
    
        return result

solution = Solution()

print(solution.minWindow('ADOBECODEBANC', 'ABC')) # Result BANC
print(solution.minWindow('ADOZZZBECODEBAAAABCNC', 'ABC')) # Result ABC
print(solution.minWindow('ADOBECABODEBANC', 'ABC')) # Result CAB

print(solution.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd")) # Result abbbbbcdd

# print(solution('xxxzzzsss', 'ABC'))