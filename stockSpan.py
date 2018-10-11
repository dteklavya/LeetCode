#!/usr/bin/env python
# Needs Python 3.x




def stockSpan(a):
    result = []
    st = []
    
    for i, v in enumerate(a):
        count = 1
        while st and a[i] >= a[st[-1]]:
            print("cmp:", v, a[st[-1]], "count", count, st, result)
            j = st.pop()
            print("Eqn: ", i, j, result[j])
            # Following is a redundant line of code as the calc is repeated.
            count = i - j + result[j]
        st.append(i)
        result.append(count)
    print(result)
    

a = [100, 80, 60, 70, 60, 75, 85]
stockSpan(a)
