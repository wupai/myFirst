'''
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
'''
def jdsxh(n):
    i=n//100
    j=n//10%10
    k=n%10
    tmp=str(n)
    if n==i**3+j**3+k**3:
        return True
    return False

for i in range(100,1000):
    if jdsxh(i):
        print(i)