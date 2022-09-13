
class auto:
    _puertas = 0

    def __init__(self, cantPuertas):
        if cantPuertas > 5:
            self._puertas = 4
        else:
            self._puertas = cantPuertas

    def getPuertas(self):
        return self._puertas

auto1 = auto(5)
auto2 = auto(10)

print(auto1.getPuertas())
print(auto2.getPuertas())