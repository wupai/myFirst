'''
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
则表明此数不是素数，反之是素数。
'''
import math

def jdprime(n):

    for i in range( 2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
sum=0
for i in range(1,200+1):
    if jdprime(i):
        sum+=1
        print('%6d'%i, end='' )
        if sum%10==0:
            print()
print()
print("总共有%d个素数"%sum)
