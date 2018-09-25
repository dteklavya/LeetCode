#!/usr/bin/env python
# Needs Python 3.x


from math import factorial

class Solution:
    def sumOfSubarrayMinimums(self, a):
        start, end = 0, 0
        resulta = []
        lena = len(a)
        
        mins = []
        
        fastsum = 0
        count = 0
        
        for start in range(lena):
            for end in range(lena, -1, -1):
                if len(a[start:end]) >= 1:
                    resulta.append(a[start:end])
                    mins.append(min(a[start:end]))
                    fastsum += min(a[start:end])
                    count += 1
        print(resulta)
        rsum = 0
        for i in resulta:
            rsum += min(i)
        print("Sum of mins: ", rsum, " and fast one: ", fastsum, " in count: ", count)
        print(a, "Subarray mins: ", mins)
        
        
    def faster(self, a):
        track = {}
        llo = []
        
        lena = len(a)
        
        lc = 0
        total = 0
        
        for i in range(lena-1, -1, -1):
            llo.append([a[i]])
            total += a[i]
            if i != 0:
                for j in range(i-1, -1, -1):
                    lc += 1
#                     print("(" + str(i) + ", " + str(j) + ")", " sliced: ", str(j) + ':' + str(i+1), a[j:i+1])
                    if i - j == 1:
                        track[(i, j)] = min(a[j:i+1])
                    else:
                        track[(i, j)] = min(a[j], track[i, j+1])
                    total += track[(i, j)]
                    llo.append(a[j:i+1])
        print(a, track)
        print(llo)
        print("Loop count: ", lc, " Sum: ", total)
        return total
        
        
s = Solution()
a = [3, 1, 2, 4]
# a = [48,87,27]
a = [1, 2, 3, 4, 5]
# s.sumOfSubarrayMinimums(a)
s.faster(a)

def prefix_sums(a):
    n = len(a)
    p = [0] * (n+1)
    for i in range(1, n+1):
        p[i] = p[i-1] + a[i-1]
    print(p)
    return p

# prefix_sums([2, 3, 7, 5, 1, 3, 9])

