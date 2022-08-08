import typing

from models.Monstruos.Tonyn import Tonyn
from models.Monstruos.Arnaldor import Arnaldor

if typing.TYPE_CHECKING:
    from models.Monstruos.Monstruo import Monstruo


def recibirDanoTest(montruoAtacante: 'Monstruo'):
    tonyn = Tonyn('Tonyn')
    vidaInicial = tonyn.vidaActual
    tonyn.eventoObservable.subscribe(lambda evento: print(evento))

    for _ in range(3):
        montruoAtacante.atacar(tonyn)

    assert tonyn.vidaActual < vidaInicial
    assert tonyn.vidaActual == 0


def tests():
    recibirDanoTest(Arnaldor('Arnaldor'))
