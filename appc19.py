import libreria
import os
#se necesita saber los años de estudio en la primaria y secundaria
#p=primaria     s=secundaria
p=int(os.sys.argv[1])
s=int(os.sys.argv[2])

msg=libreria.a_e(p,s)
print("los años de estudio hasta la actualidad son:", msg)
