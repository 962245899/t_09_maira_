import libreria
import os
#se quiere saber cuantos cursos lleva a lo largo de la carrera universitaria
#tc=total de cursos     cc=cursos de la carrera
tc=int(os.sys.argv[1])
cc=int(os.sys.argv[2])

msg=libreria.t_cursos(tc,cc)
print("el total de cursos de ing. electronica son:", msg)
