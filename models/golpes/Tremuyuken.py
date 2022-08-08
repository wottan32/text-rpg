from models.golpes.Golpe import Golpe


class Tremuyuken(Golpe):

    def getAttackPoints(self) -> int:
        return 2

    def __str__(self) -> str:
        return "Tonyn remuyuken"
