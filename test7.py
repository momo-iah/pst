import math
money = int(input())
change = [100, 50, 20, 10, 5, 2, 1]
for x in change:
    z = money / x
    if f >= 0:
        
        f , s = math.modf(z)
        print (s,'from',x)