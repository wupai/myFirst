'''
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
程序分析：请抓住分子与分母的变化规律。
'''

total=[]
fenmu=1
fenzi=2

for i in range(0,20):
    total.append(fenzi/fenmu)
    s=fenmu
    fenmu=fenzi
    fenzi=s+fenzi
print(total)
print(sum(total))

from functools import reduce
a = 2.0
b = 1.0
l = []
for n in range(1,21):
    l.append(a / b)
    b,a = a,a + b

print(reduce(lambda x,y: x + y,l))

