
class vehiculo:
    _patente = ""

    def getPatente(self):
        return self._patente

class auto(vehiculo):
    _puertas = 0

    def __init__(self, puertas, patente):
        self._puertas = puertas
        self._patente = patente

    def getPuertas(self):
        return self._puertas

auto1 = auto(4, "AAA 134")

print(f'La patente es {auto1.getPatente()}')
print(f'Tiene {auto1.getPuertas()} puertas')