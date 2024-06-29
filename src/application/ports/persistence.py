from abc import ABC, abstractmethod

class port(ABC):

    @abstractmethod
    def read(**constants):
        """
        Restituisce True se la stringa è un indirizzo email valido, altrimenti False.

        Args:
            file (str): La stringa da verificare come indirizzo email.

        Returns:
            str: True se la stringa è un indirizzo email valido, altrimenti False.
        """
        pass

    @abstractmethod
    async def create(**constants):
        pass

    @abstractmethod
    async def delete(**constants):
        pass

    @abstractmethod
    async def write(**constants):
        pass

    @abstractmethod
    async def tree(**constants):
        """
        Restituisce True se la stringa è un indirizzo email valido, altrimenti False.

        Args:
            path (str): La stringa da verificare come indirizzo email.

        Returns:
            tuple: True se la stringa è un indirizzo email valido, altrimenti False.
        """
        pass