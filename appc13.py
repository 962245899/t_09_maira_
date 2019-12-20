import libreria
import os
#el comedor universitario calcula cuantas raciones de comida entrega
ra=int(os.sys.argv[1])
al=int(os.sys.argv[2])
dia=int(os.sys.argv[3])

msg=libreria.comidas_entregadas(ra,al,dia)
print("las raciones entregadas son:", msg)
