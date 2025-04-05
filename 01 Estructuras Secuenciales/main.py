#Actividades
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print('"Hola mundo!."')

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingrese su nombre : ")
print(f"Hola {nombre}")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre : ")
apellido = input("Ingrese su apellido : ")
edad = input("Ingrese su edad : ")
residencia = input("Ingrese su lugar de residencia : ")
print(f"Hola soy {nombre} {apellido}, tengo {edad} y vivo en {residencia} ")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = int(input("Ingrese el radio del circulo para saber su area y su perimetro : "))
area = 3.14*(radio**2)
perimetro = 2*3.14*radio

print(f"El Area es de {area} y el perimetro es de {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale

segundos = int(input("Ingrese la cantidad de segundos para saber si equivalencia en horas : "))
horas = float(segundos/60)
print(f"{segundos} segundos equivalen a {horas} horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

num = int(input("Ingrese un numero del 1 al 9 "))
print(f" La tabla de multiplicar de {num} es :")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese un numero distinto al 0 : "))
num2 = int(input("Ingrese otro numero distinto a 0 : "))
suma = num1 + num2
resta = num1 - num2
division = num1/num2
multiplicacion = num1*num2

print(f"Las operaciones aritmeticas basicas de ambos numeros son : suma = {suma}, resta = {resta}, division = {division}, multiplicacion = {multiplicacion} ")
#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:
#𝐼𝑀𝐶 =
#𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
#(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)
#2

peso = float(input("Ingrese su peso en Kilogramos : "))
altura = float(input("Ingrese su altura en metros : "))
imc = peso / (altura)**2
print(f"Su IMC es de {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =
#9
#5
#. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

Celsius = int(input("Ingrese la temperatura en Grados Celsius para obtener la equivalencia en grados Farenheit : "))
faren = 9/5*Celsius+32
print(f"La temperatura en grados fahrenheit es de : {faren} ")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

num1 = float(input("Ingrese un numero : " ))
num2 = float(input("Ingrese un numero : " ))
num3 = float(input("Ingrese un numero : " ))

promedio = (num1+num2+num3)/3

print(f"El promedio de estos numeros es de {promedio}")
