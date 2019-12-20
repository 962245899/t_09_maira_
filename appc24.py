import libreria
import os
#se quiere saber lo recaudado en la venta de desayuno
#so=soya        qu=quinua
so=int(os.sys.argv[1])
qu=int(os.sys.argv[2])
msg=libreria.venta_desayuno(so,qu)
print("el total recaudado:", msg)
