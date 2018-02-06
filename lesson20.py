'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

def bounce(n):
    height=100
    bounce_meters=0
    bounce_total=height
    for i in range(1,n+1):
        bounce_total += 2 * bounce_meters
        bounce_meters=height*(1/2)**i
        print(i,bounce_meters,bounce_total)

    return bounce_meters,bounce_total

print(bounce(10))

