import libreria
import os
#se quiere saber cuantos paquetes de pañuelos hay en un producto
#pap=pañuelos por paquete       top=total de paquetes
pap=int(os.sys.argv[1])
top=int(os.sys.argv[2])

msg=libreria.t_paños(pap,top)
print("el total de pañuelos es:", msg)
