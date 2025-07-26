class Fuente():
    def reproducir(self):
        pass

class MP3(Fuente):
    def reproducir(self):
        print("Reproduciendo desde MP3")
    
class CD(Fuente):
    def reproducir(self):
        print("Reproduciendo desde CD")
    
class Console(Fuente):
    def reproducir(self):
        print("Reproduciendo desde consola")

class Reproductor():
    def __init__(self):
        self.fuente = MP3()

    def cambiar_fuente(self, nueva_fuente):
        self.fuente = nueva_fuente

    def reproducir(self):
        self.fuente.reproducir()



reproductor = Reproductor()
reproductor.reproducir()

reproductor.cambiar_fuente(CD())
reproductor.reproducir()

reproductor.cambiar_fuente(Console())
reproductor.reproducir()