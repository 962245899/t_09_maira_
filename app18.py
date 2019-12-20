import libreria
import os
#calcular la distancia
#ve=velocidad    ti=tiempo
ve=int(os.sys.argv[1])
ti=int(os.sys.argv[2])
msg=libreria.calcular_distancia(ve,ti)
print("la distancia es:", msg)
