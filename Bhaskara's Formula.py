#A,B,C = input().split()
#A=float(A)
#B=float(B)
#C=float(C)
# A,B,C = float(input().split())
#print(A,B,C)
#print(type(A),type(B),type(C))

#if (A<=0 or B<=0 or C<0): print ('Impossivel calcular')
#else:
#    D = ((B**2) - (4*A*C))
#    E = pow(D, .5)
#    F = (-B + E) / (2 * A)
#    G = (-B - E) / (2 * A)
#    F=float(F)
#    G=float(G)
#    print('R1 =', "%.5f"%F)
#    print('R2 =', "%.5f"%G)

A,B,C = list(map(float,input().split()))
d = B * B - 4 * A * C
e = pow(d, .5)
if (d < 0 or A == 0):
    print("Impossivel calcular")
else:
    f = (-B + e) / (2 * A)
    g = (-B - e) / (2 * A)
    print("R1 = %.5lf"%f)
    print("R2 = %.5lf"%g)
