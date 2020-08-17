table ={1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50}

x,y= input().split()

x = int(x)
y = float(y)
#print (x,type(x))
z = table[x]
#print (z)
#print(type(z))

v = float(z) * y
print ('Total: R$','%.2f' % v)


