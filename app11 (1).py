import libreria
import os
#se calcula el costo del tratamiento de dientes de cada mes
co=int(os.sys.argv[1])
mes=int(os.sys.argv[2])

msg=libreria.tratamiento_dientes(co,mes)
print("el costo del tratamiento de dientes es:", msg)
