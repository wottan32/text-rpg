import typing

from rx.subject import Subject

if typing.TYPE_CHECKING:
    from models.Monstruos.Jugador import Jugador
    from models.Monstruos.Monstruo import Monstruo
    from models.Monstruos.Tonyn import Tonyn
    from models.Monstruos.Arnaldor import Arnaldor
    from models.eventos.Evento import Evento


class Juego:

    def __init__(self, jugador: 'Jugador', monstruo: 'Monstruo', tonyn: 'Tonyn', arnaldor: 'Arnaldor'):
        self.jugador = jugador
        self.monstruo = monstruo
        self.tonyn = tonyn
        self.arnaldor = arnaldor

        self.jugadorDisposable = self.jugador.eventoObservable.subscribe(self.aceptarEvento)
        self.monstruoDisposable = self.monstruo.eventoObservable.subscribe(self.aceptarEvento)

        self.tonynDisposable = self.tonyn.eventoObservable.subscribe(self.aceptarEvento)
        self.arnaldorDisposable = self.arnaldor.eventoObservable.subscribe(self.aceptarEvento)

        self.resultado: Subject[bool] = Subject()

    def liberar(self) -> None:
        self.jugadorDisposable.dispose()
        self.monstruoDisposable.dispose()
        self.tonynDisposable.dispose()
        self.arnaldorDisposable.dispose()

    def ganar(self) -> None:
        self.liberar()
        self.resultado.on_next(True)
        self.resultado.on_completed()

    def perder(self) -> None:
        self.liberar()
        self.resultado.on_next(False)
        self.resultado.on_completed()

    def aceptarEvento(self, evento: 'Evento') -> None:
        evento.visitarJuego(self)

    def interaccion(self, jugador: 'Jugador', monstruo: 'Monstruo', tonyn: 'Tonyn', arnaldor: 'Arnaldor') -> str:
        self.jugador = jugador
        self.monstruo = monstruo
        self.tonyn = tonyn
        self.arnaldor = arnaldor

        return "{} recibió daño ".format(self.monstruo.nombre, self.jugador.golpe.nombre)

    def jugadorAtaca(self) -> str:
        return self.interaccion(self.jugador, self.monstruo, self.tonyn, self.arnaldor)

    def comenzar(self) -> None:
        self.jugador.atacar(self.monstruo)

    def estaVivo(self) -> bool:
        return self.monstruo.vida > 0
