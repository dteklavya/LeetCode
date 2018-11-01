#!/usr/bin/env python
# This needs Python 3.x

import unittest

class Solution:

    def allAnagrams(self, s, t):
        if not t or not s:
            return []
        
        tdict = {}
        odict = {}
        for i in t:
            odict[i] = odict.get(i, 0) + 1
            
        l, r = 0, 0
        result = []
        lens = len(s)
        lent = len(t)
        count = 0
        
        while r < lens:
            endchar = s[r]
            if endchar in odict:
                tdict[endchar] = tdict.get(endchar, 0) + 1
                count += 1
#             print(endchar, odict, tdict)
                
            while count == lent:
                if r - l + 1 == lent and tdict == odict:
                    result.append(r - lent + 1)
                startchar = s[l]
                if startchar in odict:
                    tdict[startchar] = tdict.get(startchar, 0) - 1
                    count -= 1
#                     print(startchar, tdict)
                l += 1
            r += 1
    
        return result

solution = Solution()
 
# print(solution.allAnagrams('cbaebabacd', 'abc')) # Result [0, 6]
# 
# print(solution.allAnagrams('abab', 'ab')) # Result [0, 1, 2]

# print(solution.allAnagrams('cbaebabacd', 'ab')) # Result [1, 4, 5, 6]


class TestAllAnagramsInString(unittest.TestCase):
    def test_allAnagrams(self):
        solution = Solution()
        s, t = 'cbaebabacd', 'abc'
        self.assertEqual(solution.allAnagrams(s, t), [0, 6], 'Failed test 1')
        s, t = 'abab', 'ab'
        self.assertEqual(solution.allAnagrams(s, t), [0, 1, 2], 'Failed test 2')
        s, t = 'cbaebabacd', 'ab'
        self.assertEqual(solution.allAnagrams(s, t), [1, 4, 5, 6], 'Failed test 3')
        
        
        