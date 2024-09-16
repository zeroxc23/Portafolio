import random

numfound= 0
minNum=1
maxNum=20

print("Hola cual es tu nombre?: ")
user=input()

Number= random.randint(minNum, maxNum)
print("Bueno, " + user + " Estoy pensando un numero entre " + str(minNum) + " y " + str(maxNum) )

while numfound<:
    print("Intenta adivinar el numero: ")
    intento=int(input())

    numfound= numfound+ 1

    if intento < Number:
        print("El numero que intentaste es muy bajo, intenta de nuevo")
    if intento > Number:
        print("El numero que intentaste es muy alto, intenta de nuevo")
    if intento == Number:
        break

if intento == Number:
    numfound=str(numfound)
    print("¡Felicidades! " + user + " Has adivinado el numero en " + numfound + " intentos")


