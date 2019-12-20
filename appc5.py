import libreria
import os

m=int(os.sys.argv[1])
n=int(os.sys.argv[2])
x=int(os.sys.argv[3])
y=int(os.sys.argv[4])
a=(m+n)
b=(x+y)

menor=libreria.menor(b,a)
print("El menor entre", a, " y", b, " es:", menor)
