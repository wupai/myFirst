from PIL import Image
import os
serarr = '''@#$%&?*aeoc=<{[(/l|!-_:;,."'^~` '''
count = len( serarr )


def toText(image_file):  # 此函数不能输入 gif 文件
    image_file = image_file.convert( "L" )  # 转灰度
    asd = ''  # 储存字符串
    for h in range( 0, image_file.size[1] ):  # h
        for w in range( 0, image_file.size[0] ):  # w
            gray = image_file.getpixel( (w, h) )
            asd = asd+serarr[int( gray/(256/(count-1)) )]
        asd = asd+'\r\n'
    return asd


def toText2(image_file):
    asd = ''  # 储存字符串
    for h in range( 0, image_file.size[1] ):  # h
        for w in range( 0, image_file.size[0] ):  # w
            r,g,b  = image_file.getpixel( (w, h) )
            gray =  r*0.299+g*0.587+b*0.114
            asd = asd+serarr[int( gray/(256/(count-1)) )]
        asd = asd+'\r\n'
    return asd


image_file = Image.open( r"c:\1.jpg" )  # 打开图片
image_file = image_file.resize( (int( image_file.size[0]*0.4 ), int( image_file.size[1]*0.2 )) )  # 调整图片大小
print(u'Info:', image_file.size[0], ' ', image_file.size[1], ' ', count)
tmp = open( r'c:\tmp.txt', 'w' )
tmp.write( toText2( image_file ) )
tmp.close( )
