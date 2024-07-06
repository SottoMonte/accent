from kink import di
import application.manager.manager as manager

'''
Una classe chiamata “locator” può avere diverse funzioni a seconda del contesto in cui viene utilizzata. Ecco alcune possibilità:

Locator per oggetti o risorse: In programmazione, un “locator” potrebbe essere utilizzato per individuare e gestire oggetti o risorse. Ad esempio, un locator potrebbe restituire l’indirizzo di memoria di un oggetto o la posizione di un file su disco.
Locator per servizi di localizzazione: In ambito geospaziale o di servizi di localizzazione, un “locator” potrebbe essere utilizzato per tradurre indirizzi o coordinate geografiche in posizioni sulla mappa o viceversa.
Locator per test di automazione: In test di automazione o framework di test, un “locator” è spesso utilizzato per identificare elementi dell’interfaccia utente (come pulsanti, campi di input o elementi di navigazione) all’interno di un’applicazione o di una pagina web.
Locator per risorse di sistema: In sistemi operativi o ambienti di sviluppo, un “locator” potrebbe essere utilizzato per individuare risorse di sistema come file di configurazione, librerie o percorsi di esecuzione.
'''

# nome="Risorsa1", tipo="File", posizione="/percorso/della/risorsa1"
# entita="file", driver="File", profile="local" posizione="/home/asd/accent/src/domain/views/tab.xml" policy=""
# entita="user", location="User" driver="File" policy="" profile="erp"

class locator(manager.port):
    ports = ['persistence']

    async def __call__(self,**constants):
        if 'module' in constants:
            return await self.services[0].read(file=constants['module'])
        pass

    async def service(self,**constants):
        if 'module' in constants:
            return await self.services[0].read(file=constants['module'])
        pass

    async def description(self,**constants):
        if 'module' in constants:
            return await di['persistence'].read(file=constants['module'])
        pass

    async def benchmark(self,**constants):
        if 'module' in constants:
            return await di['persistence'].read(file=constants['module'])
        pass

    async def effort(self,**constants):
        if 'module' in constants:
            return await di['persistence'].read(file=constants['module'])
        pass