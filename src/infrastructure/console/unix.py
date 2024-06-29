import application.ports.console as port
import asyncio

class console(port.port):

    def __init__(self):
        pass

    async def exe(self,**constants):
        proc = await asyncio.create_subprocess_exec(**constants,
        stdout=asyncio.subprocess.PIPE, 
        stderr=asyncio.subprocess.PIPE)
        return await proc.communicate()