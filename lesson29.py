'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
numlen = 1
def cal_grade(n):  # 利用递归算法，缺点是需要全局变量统计位数
    global numlen
    print(n % 10)
    n //= 10
    if n < 10:
        print(n)
        return numlen
    numlen += 1
    return cal_grade(n)

def cal_grade1(n):
    numlen = 1
    while (n >= 10):
        print(n % 10)
        n //= 10
        numlen += 1
    print(n)
    return numlen


if __name__ == '__main__':
    m = int(input('请输入一个整数：'))
    print('这个数是：%s位数'%cal_grade1(m))