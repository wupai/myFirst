'''
题目：利用递归方法求5!。
程序分析：递归公式：fn=fn_1*4!
'''
import sys


def calN(n):
    if n == 1:
        return 1
    return calN(n - 1) * n


if __name__ == '__main__':
    w = 50
    s = calN(w)
    print(s)

