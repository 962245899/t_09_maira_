import libreria
import os
# calcular la velocidad
#di=distancia    ti=tiempo
di=int(os.sys.argv[1])
ti=int(os.sys.argv[2])
msg=libreria.calcular_velocidad(di,ti)
print("la velocidad es:", msg)
