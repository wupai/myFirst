'''题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，
问每个月的兔子总数为多少？'''

def calhabit(n):
    f1= 1
    f2=1
    for i in range(1,n+1):
        print('%3d:%12d%3d:%12d'%(2*i-1,f1,2*i,f2),end='')
        if i%2==0:
            print()
        f1=f1+f2
        f2=f1+f2
    return f1,f2


print(calhabit(21))