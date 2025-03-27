#Actividad 1 
print ("Hola mundo")

#Actividad 2
nombre = input("Ingrese su nombre: ")
print (f"Hola {nombre}!")

#Actividad 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("ingrese su edad: ")
Pais = input("Ingrese su pais: ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {Pais}")

#Actividad 4
radio = int(input("Ingrese el radio del circulo: "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print (f"El area del circulo es: {area}, el perimetro es: {perimetro}")

#Actividad 5
tiempo = int(input("Ingrese la cantidad de segundos: "))
horas = tiempo /3600
print (f"La cantidad de segundo equivale a {horas} horas")

#Actividad 6
numero = int(input("Ingrese un numero: "))
print ("Tabla de multiplicar: ")
for i in range(1,11):
    print (i*numero)

#Actividad 7
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
print ("La suma de los numeros es: ",(a+b))
print ("La resta de los numeros es: ",(a-b))
print ("La multiplicacion de los numeros es: ",(a*b))
print ("La division de los numeros es: ",(a/b))

#Actividad 8
altura = float(input("Ingrese su altura (en metros): "))
peso = int(input("Ingrese su peso: "))
imc = peso / (altura**2)
print (f"El IMC es: {imc}")

#Actividad 9
celsius = int(input("Ingrese la temperatura en grados celcius: "))
Fahrenheit = celsius*(9/5) + 32
print (f"La temperatura en Fahrenheit es: {Fahrenheit}")

#Actividad 10
a = int (input("Ingrese su primer numero: "))
b = int (input("Ingrese su segundo numero: "))
c = int (input("Ingrese su tercer numero: "))
promedio = (a+b+c)/3
print (f"El promedio de los 3 numeros es: {promedio}")


