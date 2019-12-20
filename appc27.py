import libreria
import os
#juan y calor tienen gastos en sus hogares se calculará quien gasta mas
#gj=gastos juan     gc=gastos carlos
gj=int(os.sys.argv[1])
gjd=int(os.sys.argv[2])
gc=int(os.sys.argv[3])
gcd=int(os.sys.argv[4])
#processing
juan=(gj+gjd)
carlos=(gc+gcd)

#
msg=libreria.mayor_gastos(juan,carlos)
print("el mayor gasto a la semana es:", msg)
