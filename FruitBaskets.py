#!/usr/bin/env python
# This needs Python 3.x


class Solution:
    def maxFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        
        maxfruits, count, distinct_count = 0, 0, 0
        seen = dict()
        
        start, end = 0, 0
        
        for end in range(len(tree)):
            if tree[end] in seen:
                seen[tree[end]] += 1
            else:
                seen[tree[end]] = 1
                distinct_count += 1
            count += 1
                
            while distinct_count > 2:
                count -= 1
                if tree[start] in seen:
                    seen[tree[start]] -= 1
                if seen[tree[start]] == 0:
                    distinct_count -= 1
                    del(seen[tree[start]])
                start += 1
                
            maxfruits = max(maxfruits, count)
        return maxfruits
    

s = Solution()
s.maxFruit([1, 2, 1])
s.maxFruit([0, 1, 2, 2])
s.maxFruit([1,2,3,2,2])
s.maxFruit([3,3,3,1,2,1,1,2,3,3,4])