import abc


class Golpe(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getAttackPoints(self) -> int:
        pass

    @abc.abstractmethod
    def __str__(self) -> int:
        pass
