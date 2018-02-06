'''
题目：对10个数进行排序。
'''

def sortnum(L1):
    L = L1[:]
    for i in range(len(L)-1):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]


    return L


L =[11,3,7,4,6,5,8,9,2,1]
print(sortnum(L))
print(L)

