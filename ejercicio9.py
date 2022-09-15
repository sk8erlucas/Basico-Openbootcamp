
class Persona:
    edad = 0
    nombre = ""
    telefono = ""

class Cliente(Persona):
    credito = 0

    def __init__(self, edad, nombre, telefono, credito):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono
        self.credito = credito
    
    def __str__(self):
        return f'La edad del cliente {self.nombre} es de {self.edad}. Su telefono es {self.telefono} y su credito es de {self.credito}'

class Trabajador(Persona):
    salario = 0

    def __init__(self, edad, nombre, telefono, salario):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono
        self.salario = salario
    
    def __str__(self):
        return f'La edad del trabajador {self.nombre} es de {self.edad}. Su telefono es {self.telefono} y su salario es de {self.salario}'




nuevoCliente = Cliente(36, "Lucas", "15-1111-6491", 100000000)
print(nuevoCliente)

nuevoTrabajador = Trabajador(36, "Lucas", "15-1111-6491", 100000000)
print(nuevoTrabajador)