#Trabajo practico numero 4 estructuras repetitivas

import random

#Act 1.
for i in range(101):
    print(i)

#Act 2.

comienzo = int(input("Ingresa el primer valor: "))
final = int(input("Ingresa el segundo valor: "))

suma = sum(range(comienzo + 1, final)) 
print(f"La suma de los números entre {comienzo} y {final} es: {suma}")

#Act 3.

sumaTotal = 0

while True:
    numero = int(input("Ingresa un número entero (0 para detener): "))
    if numero == 0:
        break
    sumaTotal += numero

print(f"La suma total es: {sumaTotal}")

#Act 4

numero_aleatorio = random.randint(0, 9)
intentos = 0
acertado = False

while not acertado:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        acertado = True
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
    else:
        print("Intenta de nuevo.")

#Act 5

for i in range(100, -1, -2):  
     print(i)


#Act 6

numero = int(input("Ingresa un número entero positivo: "))
suma = sum(range(numero + 1)) 
print(f"La suma de los números entre 0 y {numero} es: {suma}")

#Act 7

cantidad = 100 
pares = 0
impares = 0
positivos = 0
negativos = 0

for _ in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

#Act 8

cantidad = 100 
sumaTotal = 0

for _ in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    sumaTotal += numero

media = sumaTotal / cantidad
print(f"La media de los {cantidad} números es: {media}")

#Act 9

numero = input("Ingresa un número: ")


if numero.startswith('-'):
    numeroInvertido = '-' + numero[:0:-1]
else:
    numeroInvertido = numero[::-1]

print(f"Número invertido: {numeroInvertido}")