#!/usr/bin/env python
# Needs Python 3.x


# n = int(input())
# a = [int(i) for i in input().split()]


# n = 4
a = [3, 1, 2, 4]
# a = [48,87,27]
# a = [1, 2, 3, 4]

n = len(a)

b = [0] * (n+1)

l = [i for i in range(n+2)]
r = [i for i in range(n+2)]

ans = 0

print(b, l, r)

# Calculation indexes for all items in a and storing indexes in b
for i in range(n):
    b[ a[i] ] = i

print(b)
print()

for i in range(n, 0, -1):
    m = b[i]
    x, y = l[m], r[m]
    ans += i * (m - x + 1) * (y - m + 1)
    print('i=', i, 'm=', m, 'x=', x, 'y=', y, 'calculations = ', str(i) + ' * ' + str((m - x + 1)) + ' * ' + str((y - m + 1)))
    print()
    
    l[y+1], r[x-1] = x, y
    
    print(ans, l, r)
    print()
print(ans)
