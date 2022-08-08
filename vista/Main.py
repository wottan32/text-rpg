from models.Monstruos.Tonyn import Tonyn
from models.Monstruos.Arnaldor import Arnaldor


class Main:
    def __init__(self):
        self.tonyn = self.crearTonyn()
        self.arnaldor = self.crearArnaldor()
        self.juego = self.Juego(self.tonyn, self.arnaldor)

    def crearTonyn(self, golpe) -> Tonyn:
        nombre = "Tonyn"
        golpe = self.crearGolpe()
        return Tonyn(nombre, golpe)

    def crearArnaldor(self, golpe) -> Tonyn:
        nombre = "Arnaldor"
        golpe = self.crearGolpe()
        return Tonyn(nombre, golpe)

    def comenzar(self) -> None:
        self.iniciarVistaCombate()
        self.iniciarVistaGanaroPerder()
        self.juego.comenzar()

    def iniciarVistaCombate(self) -> None:
        self.juego.tonyn.eventoObservable.subscribe(self.tonynAtaca)
        self.juego.arnaldor.eventoObservable.subscribe(self.arnaldorAtaca)
        pass

    def iniciarVistaGanaroPerder(self) -> None:
        self.juego.resultado.subscribe(self.ganarPerder)
        pass


if __name__ ==  '__main__':
    print("buienvenido a la Talana Kombat")
    main = Main()
