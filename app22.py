import libreria
import os
#calcular el tiempo
#di=distancia    ve=velocidad
di=int(os.sys.argv[1])
ti=int(os.sys.argv[2])
msg=libreria.calcular_tiempo(di,ti)
print("el tiempo calculado es:", msg)
