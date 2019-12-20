import libreria
import os
#se calcula el peso de un bloque
#ma=masa    gr=gravedad
ma=int(os.sys.argv[1])
gr=int(os.sys.argv[2])
msg=libreria.peso_bloque(ma,gr)
print("el peso de un bloque es:", msg)
