#!/usr/bin/env python
# Needs Python 3.x


def solution(a):
    odd, even = [], []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd