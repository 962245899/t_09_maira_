import libreria
import os
#se suman el total de paginas de dichos libros
la=int(os.sys.argv[1])
le=int(os.sys.argv[2])
li=int(os.sys.argv[3])

msg=libreria.total_de_paginas(la,le,li)
print("el total de libros de paginas es:", msg)
