import libreria
import os
#se calcula la fuerza del bloque ejercida
#ma=masa    ac=aceleracion
ma=int(os.sys.argv[1])
ac=int(os.sys.argv[2])
msg=libreria.fuerza_bloque(ma,ac)
print("la fuerza de un bloque es:", msg)
