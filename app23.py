import libreria
import os
#calcular la presion
#f=fuerza    a=area
f=int(os.sys.argv[1])
a=int(os.sys.argv[2])
msg=libreria.calcular_presion(f,a)
print("el calculo del la presion es:", msg)
