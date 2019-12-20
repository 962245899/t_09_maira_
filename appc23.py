import libreria
import os
#se quiere saver el total de focos de los adornos navideños
#ul=cuantas luces trae cada adorno      tl=total de adornos
ul=int(os.sys.argv[1])
tl=int(os.sys.argv[2])

msg=libreria.l_n(ul,tl)
print("el total de luces de los adornos navideños son:", msg)
