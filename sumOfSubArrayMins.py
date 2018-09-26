#!/usr/bin/env python
# Needs Python 3.x


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
                    
                    minion = 0
                    
                    if i - j == 1 and tuple([j, i]) not in track:
                        print("(" + str(j) + ", " + str(i) + ")", " sliced: ", str(j) + ':' + str(i+1), a[j:i+1])
                        minion = min(a[j:i+1])
                        track[(j, i)] = minion
                        llo.append(a[j:i+1])
                        lc += 1
                    elif i - j > 1:
                        
                        if tuple([j, i]) not in track:
                            minion += min(a[j], track[j+1, i])
                            track[(j, i)] = minion
                            
                            llo.append(a[j:i])
                            lc += 1
                            
                        if tuple([j, i-1]) not in track:
                            print(tuple([j, i-1]), "Not in", track, a[j:i], min(a[j:i]))
                            minion += min(a[j:i])
                            track[(j, i-1)] = minion
                            
                            llo.append(a[j:i-1])
                            lc += 1
                        
                    else:
                        continue
                    total += minion
#                     llo.append(a[j:i+1])
        print(a, "\n", track, "\n")
        print(llo)
        print("Loop count: ", lc, " Sum: ", total)
        return total
        
        
s = Solution()
a = [3, 1, 2, 4]
a = [48,87,27]
a = [1, 2, 3, 4]
# s.sumOfSubarrayMinimums(a)
s.faster(a)

