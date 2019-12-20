import libreria
import os
#
co=int(os.sys.argv[1])
mes=int(os.sys.argv[2])

msg=libreria.tratamiento_brackets(co,mes)
print("el costo del tratamiento de brackets es:", msg)
