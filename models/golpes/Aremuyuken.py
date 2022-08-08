from models.golpes.Golpe import Golpe


class Aremuyuken(Golpe):

    def getAttackPoints(self) -> int:
        return 3

    def __str__(self) -> str:
        return "Arnaldor remuyuken"
