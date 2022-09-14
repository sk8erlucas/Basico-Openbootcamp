
class persona:
    _edad = 0
    _nombre = ""
    _telefono = ""

    def setEdad(self, edad):
        self._edad = edad
    def getEdad(self):
        return self._edad

    def setNombre(self, nombre):
        self._nombre = nombre
    def getNombre(self):
        return self._nombre

    def setTelefono(self, telefono):
        self._telefono = telefono
    def getTelefono(self):
        return self._telefono

persona1 = persona()

persona1.setEdad(36)
print("La edad es", persona1.getEdad())

persona1.setNombre("Lucas")
print("El nombre es", persona1.getNombre())

persona1.setTelefono("1111-1111")
print("El telefono es", persona1.getTelefono())
