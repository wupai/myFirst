'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
程序分析：关键是计算出每一项的值。
'''

def num(a,n):

    s=0
    total=0
    for i in range(n):
        s+=a*10**i
        print('%20d'%s)
        total+=s

    return total

w=int(input("请输入数a："))
n=int(input("请输入循环次数："))
s=num(w,n)
print('-'*21)
print('%20d'%s)


