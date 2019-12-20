import libreria
import os
#quiero saber cuantos sobrinos tengo en total
#sbr=sobrins      he=hermanas
sbr=int(os.sys.argv[1])
he=int(os.sys.argv[2])

msg=libreria.total_sobrinos(sbr,he)
print("el total de sobrinos es:", msg)
