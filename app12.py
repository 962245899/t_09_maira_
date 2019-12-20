import libreria
import os

#se contabilizan las horas de estudio de matematicas
#hd=horas diarias       di=cdias
hd=int(os.sys.argv[1])
di=int(os.sys.argv[2])

msg=libreria.h_estudio(hd,di)
print("las horas de estudio realizadas son:", msg)
