import libreria
import os
#el profesor calcula cuantos jalados va ver en su curso de matematica basica
ja=int(os.sys.argv[1])
mb=int(os.sys.argv[2])

msg=libreria.numeros_jalados(ja,mb)
print("el numero de jalados del curso son:", msg)
