#this method to loop in strings and do some calculations

s = input()
x=0
z= len(s) -1
while (z >= 0):
    x += int(s[z])
    z = z- 1

print (x)
