N = int(input())

h=N//3600
N=N%3600

m=N//60
N=N%60

print(str(h)+':'+str(m)+':'+str(N))