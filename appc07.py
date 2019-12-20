import libreria
import os
#r=repuestos        c=cambio de partes
o=int(os.sys.argv[1])
p=int(os.sys.argv[2])
a=int(os.sys.argv[3])
b=int(os.sys.argv[4])
#proseccing
r=(o+p)
c=(a+b)

gastos_auto=libreria.gastos_auto(r,c)
print("los gastos del auto son:", gastos_auto)
