opciones = 0

[1,2,3]

for i in opciones:
    leeropciones=["opciones"]

leeropciones= ["opcion 1"][opciones]["mantenedor de autores"]=1
leeropciones= ["opcion 2"][opciones]["reportes"]=2
leeropciones= ["opcion 3"][opciones]["salir"]=3

print("opcion 1")
print("opcion 2")
print("opcion 3")

import json

def leeropciones (opciones:int):

    with open ("opciones", mode="r") as read:
        leeropciones = json.load (read)