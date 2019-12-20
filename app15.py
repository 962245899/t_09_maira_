import libreria
import os

#se quiere saber el total de recaudacion realizados para los niños pobres
#di=dinero        pe=personas
di=int(os.sys.argv[1])
pe=int(os.sys.argv[2])

ms=libreria.recaudacion_dinero(di,pe)
print("el total de dinero es:", ms)
