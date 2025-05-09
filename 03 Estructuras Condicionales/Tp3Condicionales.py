import random
from statistics import mode, median, mean

#TP3 condicionales
#Act 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")


#Act 2

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#Act 3

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#Act 4

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


#Act 5

contraseña = input("Ingrese su contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#act 6



numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"Media: {media:.2f}, Mediana: {mediana}, Moda: {moda}")

if media > mediana > moda:
    print("Sesgo positivo")
elif media < mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Distribución no definida con precisión")

#Act 7

frase = input("Ingrese una frase o palabra: ")
if frase[-1].lower() in 'aeiou':
    frase += "!"
print(frase)


#ACt 8

nombre = input("Ingrese su nombre: ")
print("Opciones:\n1. Mayúsculas\n2. Minúsculas\n3. Primera letra mayúscula")
opcion = input("Ingrese una opción (1/2/3): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")


#Act9

magnitud = float(input("Ingrese la escala del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")


#Act 10
estacion = ""
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()

fecha = mes * 100 + dia

if hemisferio == 'N':
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Invierno"
    elif 321 <= fecha <= 620:
        estacion = "Primavera"
    elif 621 <= fecha <= 920:
        estacion = "Verano"
    else:
        estacion = "Otoño"
else:  # Hemisferio Sur
    if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
        estacion = "Verano"
    elif 321 <= fecha <= 620:
        estacion = "Otoño"
    elif 621 <= fecha <= 920:
        estacion = "Invierno"
    else:
        estacion = "Primavera"

print(f"Usted se encuentra en {estacion}")