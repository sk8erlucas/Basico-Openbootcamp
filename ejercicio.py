def suma(a, b):
    return a + b

resultado = suma(1, 2)
print(f'La suma de 1 y 2 es {resultado}')


class coche():
    puertas = 0

    def AumentarPuertas(self):
        self.puertas += 1

miCoche = coche()

miCoche.AumentarPuertas()
print(f'El coche tiene {miCoche.puertas} puerta')



    