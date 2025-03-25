print("Tabla de Multiplicar ")
num = int (input("Ingrese un numero: "))

for i in range (1,11):  # Itineramos para realizar la tabla de multiplicacion

    resultado = num * i
    print (f"{num} x {i} = {resultado }")
