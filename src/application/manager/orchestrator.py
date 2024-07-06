class orchestrator():
    services = [] # list of drivers
    policies = [] # config

    def __init__(self,**constants):
        if 'services' in constants:
            self.services = constants['services']
        if 'service' in constants:
            self.services.append(constants['service'])
        if 'policies' in constants:
            self.policies = constants['policies']

    async def __call__(self,**constants):
        if 'module' in constants:
            return await services[0].read(file=constants['module'])
        pass

    async def register(self,**constants):
        self.services.append(constants['driver'])
        return self


    async def forgetServices(self,**constants):
        return self

    async def getServices(self,**constants):
        return self.services