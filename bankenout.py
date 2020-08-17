#import math
#x = int(input())
#z = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0 , 1.0]
#s = 0.0
#for i in z:
#    c = (x / i) - (s*i)
#    f, s = math.modf(c)
#    print (s,'nota(s) de R$', i)
#    if f > 0:
#        x = f

cx = int(input())

c100 = cx // 100
x = cx % 100

c50 = x // 50
x = x % 50

c20 = x //20
x = x % 20

c10 = x // 10
x = x % 10

c5 = x // 5
x = x % 5

c2 = x // 2
x = x % 2

print (cx)
print (c100,'nota(s) de R$ 100,00')
print (c50,'nota(s) de R$ 50,00')
print (c20,'nota(s) de R$ 20,00')
print (c10,'nota(s) de R$ 10,00')
print (c5,'nota(s) de R$ 5,00')
print (c2,'nota(s) de R$ 2,00')
print (x,'nota(s) de R$ 1,00')

