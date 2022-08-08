from models.Monstruos.Monstruo import Monstruo
from models.golpes.Ataladoken import Ataladoken
from models.golpes.Aremuyuken import Aremuyuken
from models.golpes.Punetazo import Punetazo
from models.golpes.Patada import Patada


from models.eventos.ArnaldorMuere import ArnaldorMuere


class Arnaldor(Monstruo):

    def __init__(self, nombre: str):
        super().__init__('', 6, golpe=[Ataladoken, Aremuyuken, Punetazo, Patada])
        self.nombre = nombre
        self.golpe = Ataladoken
        self.golpe = Aremuyuken
        self.golpe = Punetazo
        self.golpe = Patada

    def morir(self) -> None:
        self.eventoObservable.on_next(ArnaldorMuere())
        self.eventoObservable.on_completed()
