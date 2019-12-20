import libreria
import os
#el total de edad de un hogar es
c=int(os.sys.argv[1])
s=int(os.sys.argv[2])
h=int(os.sys.argv[3])
ce=int(os.sys.argv[4])
g=int(os.sys.argv[5])

msg=libreria.t_edad(c,s,h,ce,g)
print("el total de edad del hogar es de:", msg)
