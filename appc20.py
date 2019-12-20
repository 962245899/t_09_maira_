import libreria
import os
#quiero saber cuantos primos tengo en total
#pr=primos      ti=tios
pr=int(os.sys.argv[1])
ti=int(os.sys.argv[2])

msg=libreria.t_p(pr,ti)
print("el total de primos (incyluyendote) es:", msg)
