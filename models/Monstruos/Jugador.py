from models.Monstruos.Monstruo import Monstruo
from models.golpes.Ataladoken import Ataladoken
from models.eventos.JugadorMuere import JugadorMuere


class Jugador(Monstruo):

    def __init__(self, nombre: str):
        super().__init__('', 6, Ataladoken(), Ataladoken(), Ataladoken(), Ataladoken())
        self.nombre = nombre

    def morir(self) -> None:
        self.eventoObservable.on_next(JugadorMuere())
        self.eventoObservable.on_completed()
