import libreria
import os
#se halla los meses de vida que han transcurrido
#an=años
an=int(os.sys.argv[1])
msg=libreria.mes_vida(an)
print("los meses de vida hasta el momento son:", msg)
