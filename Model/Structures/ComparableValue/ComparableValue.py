from abc import ABC, abstractmethod


class ComparableValue(ABC):
    @abstractmethod
    def __lt__(self, other) -> bool:
        pass

    @abstractmethod
    def __gt__(self, other) -> bool:
        pass

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass

    @abstractmethod
    def __le__(self, other) -> bool:
        pass

    @abstractmethod
    def __ge__(self, other) -> bool:
        pass

