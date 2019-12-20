import libreria
import os
#se hace un sorteo el que optenga el numero mayor se lleva el premio
p=int(os.sys.argv[1])
o=int(os.sys.argv[2])

ganadorr=libreria.sorteo(p,o)

print("el ganador del sorteo es:", ganadorr)
