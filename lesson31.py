'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''
theday = input('请输入一个星期日的英语：')

if (theday[0] in ('m', 'M') ):
    print("今天是星期一")
elif (theday[0] in ('T', 't')):
    if theday[1] in ('U', 'u'):
        print("今天是星期二")
    else:
        print("今天是星期四")
elif (theday[0] in ('W', 'w')):
    print("今天是星期三")
elif (theday[0] in ('F', 'f')):
    print("今天是星期五")
elif (theday[0] in ('s', 'S')):
    if theday[1] in ('U', 'u'):
        print("今天是星期日")
    else:
        print("今天是星期六")

