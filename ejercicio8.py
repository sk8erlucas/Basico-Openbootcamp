
class persona:
    _edad = 0
    _nombre = ""
    _telefono = ""

    def setEdad(self, edad):
        self._edad = edad
    def getEdad(self):
        return self._edad

persona1 = persona()

persona1.setEdad(36)
print(persona1.getEdad())

