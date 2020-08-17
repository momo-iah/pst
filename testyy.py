import math
by , cx  = math.modf(float(input()))
#print(cx,by)
cx = int(cx)
by = round(by,2)
#print(cx,by)

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

y50 = by // 0.50
y = by % 0.50
y25 = y // 0.25
y = y % 0.25
y10 = y // 0.10
y = y % 0.10
y5 = y // 0.05
y = y % 0.05

y = round(y,2) *100





print ('NOTAS:')
print (int(c100),'nota(s) de R$ 100.00')
print (int(c50),'nota(s) de R$ 50.00')
print (int(c20),'nota(s) de R$ 20.00')
print (int(c10),'nota(s) de R$ 10.00')
print (int(c5),'nota(s) de R$ 5.00')
print (int(c2),'nota(s) de R$ 2.00')
print ('MOEDAS:')
print (int(x),'moeda(s) de R$ 1.00')
print (int(y50),'moeda(s) de R$ 0.50')
print (int(y25),'moeda(s) de R$ 0.25')
print (int(y10),'moeda(s) de R$ 0.10')
print (int(y5),'moeda(s) de R$ 0.05')
print (int(y),'moeda(s) de R$ 0.01')
