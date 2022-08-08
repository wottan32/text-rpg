from models.Monstruos.Monstruo import Monstruo
from models.golpes.Ttaladoken import Ttaladoken
from models.golpes.Tremuyuken import Tremuyuken
from models.golpes.Punetazo import Punetazo
from models.golpes.Patada import Patada


from models.eventos.TonynMuere import TonynMuere


class Tonyn(Monstruo):

    def __init__(self, nombre: str):
        super().__init__('', 6, golpe=[Ttaladoken, Tremuyuken, Punetazo, Patada])
        self.nombre = nombre
        self.golpe = Ttaladoken
        self.golpe = Tremuyuken
        self.golpe = Punetazo
        self.golpe = Patada

    def morir(self) -> None:
        self.eventoObservable.on_next(TonynMuere)
        self.eventoObservable.on_completed()
