import libreria
import os
#se quiere saber el total de gaseosas vendidas
#pv=paquete de venta        paq=cuantas unidades trae cada paquete
pv=int(os.sys.argv[1])
paq=int(os.sys.argv[2])

msg=libreria.g_v(pv,paq)
print("el total de gaseosa vendidas son:", msg)
