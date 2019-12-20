import os
import libreria
#notas_examen=notas de examen por curso      cu=cursos
notas_examen=0
cu=os.sys.argv[1]
notas_examen=os.sys.argv[2]
#si las notas de los examenes son mas de 20 se le entragará una beca
if (20<notas_examen):
    print("te ganaste una beca")
else:
    print("¡sigue adelante!")
