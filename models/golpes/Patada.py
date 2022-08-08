from models.golpes.Golpe import Golpe


class Patada(Golpe):

    def getAttackPoints(self) -> int:
        return 1

    def __str__(self) -> str:
        return "Patada"
