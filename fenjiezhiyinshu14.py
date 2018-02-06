'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''
def depart(n):
    if n<2:
        return ["不满足条件，无法分解"]
    m=[]
    k=2
    while (k!=n):
        if n%k==0:
            m.append(k)
            n=n/k
        else:
            k+=1

    m.append(k)
    return m

num=int(input('请输入一个正整数：'))
s=depart(num)
w1=[str( x ) for x in s]
tmp=''
for i in w1:
    if i is w1[-1]:
        tmp=tmp+i
    else:
        tmp+=i+' * '
print("%s = %s"%(num,tmp))
