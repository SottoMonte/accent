# Policy: fast|slow|dynamic 'web o nativo' - local|
from kink import di


class presenter():
    ports = ['presentation']

    async def builder(self,**constants):
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