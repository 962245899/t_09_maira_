import libreria
import os
#se suman el total de dichos libros leidos de fisica
sa=int(os.sys.argv[1])
se=int(os.sys.argv[2])
si=int(os.sys.argv[3])
so=int(os.sys.argv[4])

msg=libreria.total_de_libros(sa,se,si,so)
print("el total de libros es:", msg)
