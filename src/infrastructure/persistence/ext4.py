import application.ports.persistence as port
import os
import aiofiles


class filesystem(port.port):

    def __init__(self):
        pass

    async def read(self,**constants):
        """
        Restituisce True se la stringa è un indirizzo email valido, altrimenti False.

        Args:
            file (str): La stringa da verificare come indirizzo email.

        Returns:
            str: True se la stringa è un indirizzo email valido, altrimenti False.
        """
        try:
            async with aiofiles.open(constants['file'], mode="r") as file:
                content = await file.read()
                return content
        except FileNotFoundError:
            return None

    async def create(self,**constants):
        pass

    async def delete(self,**constants):
        pass

    async def write(self,**constants):
        """
        Restituisce True se la stringa è un indirizzo email valido, altrimenti False.

        Args:
            file (str): La stringa da verificare come indirizzo email.

        Returns:
            str: True se la stringa è un indirizzo email valido, altrimenti False.
        """
        try:
            async with aiofiles.open(file_path, mode="r") as file:
                content = await file.read()
                return content
        except FileNotFoundError:
            return "File non trovato."

    async def tree(self,**constants):
        """
        Restituisce True se la stringa è un indirizzo email valido, altrimenti False.

        Args:
            path (str): La stringa da verificare come indirizzo email.

        Returns:
            tuple: True se la stringa è un indirizzo email valido, altrimenti False.
        """
        albero = []
        for elemento in os.listdir(constants['path']):
            percorso_completo = os.path.join(constants['path'], elemento)
            if os.path.isdir(percorso_completo):
                # Ricorsione per le sottodirectory
                #print(percorso_completo)
                print(percorso_completo)
                fs_tree = await self.tree(path=percorso_completo)
                albero.append(('dir',percorso_completo,elemento,fs_tree))
            else:
                albero.append(('file',percorso_completo,elemento))
        return tuple(albero)