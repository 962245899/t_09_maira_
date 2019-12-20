import libreria
import os
#en una donacion de frasadas se quiere saber cuantas frasadas se entregaron al año

mes=int(os.sys.argv[1])

msg=libreria.frasadas_donadas(mes)
print("las frasadas donadas al año son:", msg)
