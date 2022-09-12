
numeroIf = int(input("Ingresa un numero: "))

if (numeroIf > 0):
    print("El numero es mayor cero")
elif (numeroIf < 0):
    print("El numero es menor a cero")
else:
    print("El numero es cero")

numeroWhile = int(input("Ingresa un numero menor a 3: "))

while (numeroWhile < 3):
    numeroWhile += 1
    print(f"Numero incrementado en 1, actual {numeroWhile}")

numeroFor = 0
for numeroFor in range(0, 3):
    print(numeroFor)

estacion = input("Ingresa la estacion: ")

if (estacion == "verano"):
    print("Que calor hace en verano")
elif (estacion == "otono"):
    print("Se caen las hojas en otono")
elif (estacion == "primavera"):
    print("Como crecen las flores en primavera")
elif (estacion == "invierno"):
    print("Que frio hace en invierno")
else:
    estacion = "verano"
    print("Error en la estacion, se asgina verano")