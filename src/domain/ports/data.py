from abc import ABC, abstractmethod

class data(ABC):

    @abstractmethod
    def show(constants):
        pass

    @abstractmethod
    def create(constants):
        pass

    @abstractmethod
    def delete(constants):
        pass

    @abstractmethod
    def read(constants):
        pass