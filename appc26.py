import libreria
import os
#se quiere saber cuantos patos han nacido
#cp=crias de patos      mp=mama pata
cp=int(os.sys.argv[1])
mp=int(os.sys.argv[2])

msg=libreria.n_patos(cp,mp)
print("el numero de patos que han nacido son:", msg)
