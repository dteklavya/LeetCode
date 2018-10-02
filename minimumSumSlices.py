#!/usr/bin/env python
# Needs Python 3.x


def minimumSumSlicesUnsorted(a):
    n = max(a)
    
    b = [0] * (n+1)
    
    left = [i for i in range(n+2)]
    right = [i for i in range(n+2)]
    
    result = 0
    
    # Calculation indexes for all items in a and storing indexes in b
    for i, v in enumerate(a):
        b[ v ] = i + 1
    
    print(b)
    print()
    
    for i in range(n, 0, -1):
        if b[i] == 0:
            continue
        index = b[i]
        
        l, r = left[index], right[index]
        result += i * (index - l + 1) * (r - index + 1)
        print('i=', i, 'index=', index, 'l=', l, 'r=', r, 'calculations = ', str(i) + ' * ' + str((index - l + 1)) + ' * ' + str((r - index + 1)))
        print()
        
        left[r+1], right[l-1] = l, r
        
        print(result, left, right)
        print()
    print(result)
    return result


a = [3, 1, 2, 4]
# a = [48,87,27]
# a = [1, 2, 3, 4]

minimumSumSlicesUnsorted(a)