'''
25题目：求1+2!+3!+...+20!的和。
26题目：利用递归方法求5!。
'''

def facN(n):   # N!
    total=1
    for i in range(1,n+1):
        total*=i
    return total
def facN1(n):
    if n==1:
        return 1
    return facN1(n-1)*n

def main() :
    print('25题答案--1+2!+3!+...+20!的和为：%20s'%sum(map(facN,range(1,21))))
    print(('26题答案--5！= %s'%facN1(5)))
    
if __name__ == '__main__':
    main()
