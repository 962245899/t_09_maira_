import libreria
import os
#L=luz        A=agua
o=int(os.sys.argv[1])
p=int(os.sys.argv[2])
q=int(os.sys.argv[3])
r=int(os.sys.argv[4])
#proseccing
L=(o+p)
A=(q+r)

gastos_casa=libreria.gastos_casa(L,A)
print("los gastos de la casa son:", gastos_casa)
