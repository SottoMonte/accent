from kink import di

# nome="Risorsa1", tipo="File", posizione="/percorso/della/risorsa1"
# entita="file", driver="File", profile="local" posizione="/home/asd/accent/src/domain/views/tab.xml" policy=""
# entita="user", location="User" driver="File" policy="" profile="erp"

class locator():
    ports = ['persistence']

    async def service(self,**constants):
        if 'module' in constants:
            return await di['persistence'].read(file=constants['module'])
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