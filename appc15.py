import libreria
import os

#se quiere saber el total de donaciones realizadas para la chocolatada
#ju=juguetes        du=dulces
ju=int(os.sys.argv[1])
du=int(os.sys.argv[2])

ms=libreria.colecta_chocolatada(ju,du)
print("el total de donaciones es:", ms)
