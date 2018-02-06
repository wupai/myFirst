'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''
import  functools
def judge(n):
    m = str(n)
    return m[::-1] == m

def judge1(n):
    n1 = n
    numlen = 0
    s = []
    while (n != 0):
        m = n % 10
        n //= 10
        s .append(m)
    print(s)
    return (functools.reduce(lambda x, y: x * 10 +y , s) == n1)

    




num = int(input('请输入一个整数：'))
if judge1(num):
    print('%s是一个回文数！'%num)
else:
    print('%s不是不是就不是回文数！'%num)