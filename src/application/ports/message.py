# internal external dove viaggiano i dati

from abc import ABC, abstractmethod

class port(ABC):

    @abstractmethod
    def loader(constants):
        pass

    @abstractmethod
    async def speak(constants):
        pass

    @abstractmethod
    async def hear(constants):
        pass