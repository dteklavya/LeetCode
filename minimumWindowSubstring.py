#!/usr/bin/env python
# This needs Python 3.x


def solution(s, t):
    if not t or not s:
        return ''
    
    t_dict = {}
    for i in t:
        t_dict[i] = t_dict.get(i, 0) + 1
    odict = {i : v for i, v in t_dict.items()}
        
    l, r = 0, 0
    result = ''
    lens = len(s)
    print(t_dict)
    
    sublen = lens
    
    while r < lens:
        endchar = s[r]
        if endchar in t_dict:
            t_dict[endchar] -= 1
            
        print("Outer", s[l:r+1], t_dict)

        while sum(t_dict.values()) == 0:
            cdict = {}
            for i in s[l:r+1]:
                if i in odict:
                    cdict[i] = cdict.get(i, 0) + 1
            if r - l < sublen and cdict == odict:
                sublen = r -l
                result = s[l:r+1]
            
            startchar = s[l]
            if startchar in t_dict:
                t_dict[startchar] += 1
            print("\tInner", s[l:r+1], t_dict)
            l += 1
        r += 1

    return result

print(solution('ADOBECODEBANC', 'ABC'))
print(solution('ADOZZZBECODEBAAAABCNC', 'ABC'))
print(solution('ADOBECABODEBANC', 'ABC'))

# print(solution("aaaaaaaaaaaabbbbbcdd", "abcdd"))

exit()

def minWindowSubstring(s, t):
    if not t or not s:
        return ''
    
    t_dict = {}
    for i in t:
        t_dict[i] = t_dict.get(i, 0) + 1
    print(t_dict)
    
    o_sum = sum(t_dict.values())
    counter = sum(t_dict.values())
        
    l, r = 0, 0
    result = ''
    lens = len(s)
    
    sublen = lens
    
    while r < lens:
        endchar = s[r]
        if endchar in t_dict and t_dict[endchar] > 0:
            if counter == o_sum:
                l = r
            t_dict[endchar] -= 1
            counter -= 1

        if counter == 0:
            if r - l < sublen:
                sublen = r - l
                result = s[l:r+1]
            for i in t:
                t_dict[i] = t_dict.get(i, 0) + 1
                counter = sum(t_dict.values())
            l = r
        r += 1

    return result

print(minWindowSubstring('ADOBECODEBANC', 'ABC'))

print(minWindowSubstring('ADOZZZBECODEBAAAABCNC', 'ABC'))

print(minWindowSubstring('ADOBECABODEBANC', 'ABC'))