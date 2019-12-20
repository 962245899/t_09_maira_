import libreria
import os
#se quiere saber el total de cervezas vendidas
#cvz=cajas de cerveza        unid=cuantas unidades trae
cvz=int(os.sys.argv[1])
unid=int(os.sys.argv[2])

msg=libreria.cervezas_vendidas(cvz,unid)
print("el total de cervezas vendidas son:", msg)
