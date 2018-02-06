import math

for i in range( 10000 ):
    x = math.sqrt( i + 100 )
    y = math.sqrt( i + 268 )
    if x - math.trunc( x ) == 0 and y - math.trunc( y ) == 0:
        print( i )
