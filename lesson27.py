'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
程序分析：无。
'''


def out(s, l):
    if l == 0:
        return 0
    print(s[l - 1])
    return out(s, l - 1)


def out1(s):
    if len(s) > 0:
        print(s[-1])
        return out1(s[:-1])


if __name__ == '__main__':
    s = input('plese input a word:')
    out(s, len(s))
    out1(s)
