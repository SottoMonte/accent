from abc import ABC, abstractmethod

class port(ABC):

    @abstractmethod
    def exe(**constants):
        """
        Restituisce True se la stringa è un indirizzo email valido, altrimenti False.

        Args:
            file (str): La stringa da verificare come indirizzo email.

        Returns:
            str: True se la stringa è un indirizzo email valido, altrimenti False.
        """
        pass

