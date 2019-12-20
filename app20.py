import libreria
import os
#calcular el area del trapecio
#b1=base mayor    b2=base menor      a=altura
b1=int(os.sys.argv[1])
b2=int(os.sys.argv[2])
a=int(os.sys.argv[3])
msg=libreria.area_trapecio(b1,b2,a)
print("el area del trapeco es:", msg)
