import libreria
import os
#en una donacion de jugetes se quiere saber cuantos jugetes se netregaron al año

mes=int(os.sys.argv[1])

msg=libreria.jugetes_donados(mes)
print("los jugetes donados al año son:", msg)
