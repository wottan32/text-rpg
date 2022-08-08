import typing

import Utils

if typing.TYPE_CHECKING:
    from models.Monstruos.Tonyn import Tonyn
    from models.Monstruos.Arnaldor import Arnaldor
    from controlador.Juego import Evento



class VistaCombate:

    def __init__(self, juego:'Juego', tonyn:'Tonyn', arnaldor:'Arnaldor'):
        self.juego = juego
        self.tonyn = tonyn
        self.arnaldor = arnaldor
        self.juego.tonyn.eventoObservable.subscribe(self.tonynAtaca)
        self.juego.arnaldor.eventoObservable.subscribe(self.arnaldorAtaca)
        self.juego.resultado.subscribe(self.ganarPerder)

        self.pelear()

    def pelear(self) -> None:
        print(self.juego.jugadorAtaca(), "partida se ha iniciado")

        while self.juego.estaVivo():
            self.juego.jugador.atacar(self.juego.monstruo)
            self.juego.monstruo.atacar(self.juego.jugador)
            input("Presione enter para continuar")
            Utils.limpiarPantalla()
            self.turno()
            input("Presione enter para continuar")
            Utils.limpiarPantalla()
            self.turno()


    def turno(self) -> None:
        print(self.juego.jugadorAtaca(), "turno")
        print(self.juego.jugador)
        print(self.juego.monstruo)