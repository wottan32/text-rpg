import sys
import typing

from models.eventos.Evento import Evento

if typing.TYPE_CHECKING:
    from controlador.Juego import Juego


class MonstruoMuere(Evento):

    def visitarJuego(self, juego: 'Juego'):
        juego.perder()
        sys.exit()
