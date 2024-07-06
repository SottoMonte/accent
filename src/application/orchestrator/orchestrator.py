class orchestrator():
    services = [] # list of drivers
    policies = [] # config

    def __init__(self,**constants):
        if 'module' in constants:
            return await di['persistence'].read(file=constants['module'])
        pass

    async def __call__(self,**constants):
        if 'module' in constants:
            return await di['persistence'].read(file=constants['module'])
        pass

    async def register(self,**constants):
        return self


    async def forgetServices(self,**constants):
        return self

    async def getServices(self,**constants):
        return self.services