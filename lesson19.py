'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
'''


def depart(n):
    m = []
    w = int( n/2 )
    for k in range( 1, w+1 ):
        if n%k == 0:
            m.append( k )
    return m


for i in range( 3, 1000 ):
    # tmp=depart(i)
    # print(tmp)
    if i == int( sum( depart( i ) ) ):
        print( i )
