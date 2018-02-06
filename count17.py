'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为'\n'。
'''
#import  string
str=input("请随便输点什么，我帮你统计：\n")
numletter=0
numdigit=0
numspace=0
numother=0
for s in str:
    if s.isalpha():
        numletter+=1
    elif s.isdigit():
        numdigit+=1
    elif s.isspace():
        numspace+=1
    else:
        numother+=1

print ('char = %d,space = %d,digit = %d,others = %d' % (numletter,numspace,numdigit,numother))


