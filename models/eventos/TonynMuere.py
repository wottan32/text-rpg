from models.eventos.Evento import Evento

import typing
import sys

if typing.TYPE_CHECKING:
    from controlador.Juego import Juego


class TonynMuere(Evento):

    def visitarJuego(self, juego: 'Juego'):
        juego.perder()
        sys.exit()