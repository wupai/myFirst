'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''


def myinsert(n, L):
    L1 = L[:]
    if n > L1[-1]:
        L1.append(n)
        return L1
    min = 0
    for i, item in enumerate(L):
        if n > item:
            min = i+1
    L1.insert(min, n)
    return  L1


L= list(range(10))
print(L)
print(myinsert(8.1 ,L))

pass
pass
pass
