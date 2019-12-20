import libreria
import os

r=int(os.sys.argv[1])
s=int(os.sys.argv[2])
o=int(os.sys.argv[3])
p=int(os.sys.argv[4])

c=(r*s)
f=(o*p)

cantidad_mayor=libreria.cantidad_mayor(c,f)
print("El mayor entre", c, " y", f, " es:", cantidad_mayor)
