import abc
import typing

from rx.subject import Subject

from models.eventos.MonstruoMuere import MonstruoMuere
from models.golpes.Golpe import Golpe
from models.golpes.Aremuyuken import Aremuyuken
from models.golpes.Ataladoken import Ataladoken
from models.golpes.Punetazo import Punetazo
from models.golpes.Patada import Patada
from models.golpes.Tremuyuken import Tremuyuken
from models.golpes.Ttaladoken import Ttaladoken

if typing.TYPE_CHECKING:
    from models.eventos.Evento import Evento


class Monstruo(metaclass=abc.ABCMeta):

    def __init__(self, nombre: str, vidaMaxima: int, golpe: ['Aremuyuken', 'Ataladoken',
                 'Punetazo', 'Patada', 'Tremuyuken', 'Ttaladoken']):
        self.nombre = nombre
        self.vidaMaxima = vidaMaxima
        self.golpe = golpe
        self.vidaActual = vidaMaxima
        self.eventoObservable: Subject['Evento'] = Subject()

    def getAttackPoints(self) -> int:
        return self.golpe.getAttackPoints()

    def recibirDano(self, golpe: 'Golpe'):
        self.vidaActual -= golpe.getAttackPoints()
        if self.vidaActual <= 0:
            self.vidaActual = 0
            self.morir()

    def atacar(self, monstruoQueRecibe: 'Monstruo') -> None:
        monstruoQueRecibe.recibirDano(self.golpe)

    def morir(self) -> None:
        self.eventoObservable.on_next(MonstruoMuere())
        self.eventoObservable.on_completed()
