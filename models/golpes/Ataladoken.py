from models.golpes.Golpe import Golpe


class Ataladoken(Golpe):

    def getAttackPoints(self) -> int:
        return 2

    def __str__(self) -> str:
        return "Arnaldor taladoken"
