import libreria
import os
#se quiere saber cuanta leche se recauda
#nv=numero de vacas     nl=litros
nv=int(os.sys.argv[1])
nl=int(os.sys.argv[2])
msg=libreria.l_leche(nv,nl)
print("el total de litros de leche es:", msg)
