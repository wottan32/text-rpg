from models.golpes.Golpe import Golpe


class Punetazo(Golpe):

    def getAttackPoints(self) -> int:
        return 1

    def __str__(self) -> str:
        return "Punetazo"
