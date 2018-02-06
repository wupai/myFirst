'''
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，
c说他不和x,z比，请编程序找出三队赛手的名单。
'''
s='xyzw'
n=0
for i in range(4):
    for j in range(4):
        if i!=j:

            for k in range(4):
                n += 1
                if i!=k and j!=k:
                    if i!=s.index('x') and k!=s.index('x') and k!=s.index('z'):
                        print("a--%s    b--%s    c--%s"%(s[i],s[j],s[k]))


print(n)

for i in range(25):
    print(('*'*(2*i+1)).center(60))

for i in range(25,-1,-1):
    print(('*'*(2*i+1)).center(60))
