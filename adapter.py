from P2.Derecha import *
from P2.Izquierda import *
from constuctores import Constructor

class ConstructorAdaptado(Constructor):
    def __init__(self):
        self.der = Derecha()
        self.izq = Izquierda()

    def get_sprites(self):
        return [self.der.getDerecha(),
                self.izq.getIzquierda()]

