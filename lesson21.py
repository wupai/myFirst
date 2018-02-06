'''
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，
还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，
又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
'''

def num_peach(n): #递归算法
    if n==1:
        return 1
    return 2*(num_peach(n-1)+1)

def num_peach2(n): #迭代算法
    m=1
    for i in range(2,n+1):
        m=2*(m+1)
    return m

print(num_peach(10))