import sys
import asyncio
sys.path.append('src/application/ports')
import redis.asyncio as r
import persistence as module_persistence
import message as module_messenger

#adapter
class persistence(module_persistence.port):

    def loader(**constants):
        return r.from_url("redis://localhost:6379")

    async def create(**constants):
        data = constants['data']
        boolean = await constants['app'].broker.exists(data.identifier)

        if not boolean:
            #print(f'{worker.app.identifier}.{data.identifier}',data.value)
            #await worker.app.broker.mset({f'{worker.app.identifier}.{data.identifier}': XML(worker,data)})
            #await worker.app.broker.rpush(data.identifier, *data.value)
            print(f"NEW::{data.identifier}",data.type,data.value)
            match data.type:
                case 'list':
                    await worker.app.broker.rpush(data.identifier, *data.value)
                case 'string':
                    await constants['app'].broker.set(data.identifier, data.value)
                case 'set':
                    await constants['app'].broker.sset(data.identifier, data.value)
                case 'dict':
                    #await worker.app.broker.mset(data.value)
                    await worker.app.broker.hmset(data.identifier, data.value)
                case 'hash':
                    await worker.app.broker.hmset(data.identifier, data.value)
                case _:
                    print("ERRORE TIPO",data.type)
            
            #await SPEAK(worker,data.identifier,"event: new data")

    async def read(**constants):
        identifier = constants['id']
        boolean = await constants['app'].broker.exists(identifier)
        print(f"GET::{identifier}")
        if boolean:
            typ = await constants['app'].broker.type(identifier)
            
            match typ.decode('ascii'):
                case 'list':
                    value = await worker.app.broker.lrange(identifier, 0, -1)
                    return VARIABLE(worker,typ.decode('ascii'),identifier,[x.decode('ascii') for x in value])
                case 'string':
                    value = await constants['app'].broker.get(identifier)
                    return value
                case 'set':
                    await worker.app.broker.sadd(identifier, value)
                case 'dict':
                    return await worker.app.broker.mget(identifier)
                case 'hash':
                    value = await worker.app.broker.hgetall(identifier)
                    return VARIABLE(worker,typ.decode('ascii'),identifier,{x.decode('ascii'):value[x].decode('ascii') for x in value})
        else:
            typ = await constants['app'].broker.type(identifier)
            print(typ)
            return None

    async def update(worker,identifier,value,de=None):
        boolean = await worker.app.broker.exists(identifier)
        if boolean:
            typ = await worker.app.broker.type(identifier)
            print(f"SET::{identifier}",typ)
            match typ.decode('ascii'):
                case 'list':
                    #print('list')
                    a = await worker.app.broker.rpush(identifier, value)
                    return a
                case 'string':
                    #print('string')
                    await worker.app.broker.set(identifier, str(value))
                case 'set':
                    #print('set')
                    await worker.app.broker.sset(identifier, value)
                case 'dict':
                    #print('dict')
                    await worker.app.broker.mset(identifier,value)
                case 'hash':
                    #print('hash')
                    await worker.app.broker.hmset(identifier,value)
            await SPEAK(worker,identifier,"change event")
        else:
            await NEW(worker,de)

    async def remove(worker,identifier,start=0,end=-1):
        if await worker.app.broker.exists(identifier):
            typ = await worker.app.broker.type(identifier)
            print(f"REM::{identifier}",typ)
            match typ.decode('ascii'):
                case 'list':
                    #await worker.app.broker.lpop(identifier,2)
                    a = await worker.app.broker.ltrim(identifier,start,end)
                    return a
                    #firma_funzione = inspect.signature(worker.app.broker.ltrim)
                    #print(firma_funzione)
                case 'string':
                    #print(dir(worker.app.broker))
                    a = await worker.app.broker.delete(identifier)
                    pass
                case 'set':       
                    a = await worker.app.broker.delete(identifier)
                    return a
                case 'dict':
                    #await worker.app.broker.hdel(identifier)
                    pass
                case 'hash':
                    keys = await worker.app.broker.hkeys(identifier)
                    for key in keys:
                        id = f"{identifier}.{key.decode('ascii')}"
                        #print(id)
                        boolean = await worker.app.broker.exists(id)
                        if boolean:
                            await REM(worker,id)
                    await worker.app.broker.hdel(identifier,*[key.decode('ascii') for key in keys])

# ------------------------------------------------

class messenger(module_messenger.port):

    def __init__(self):
        self.connection = self.loader()

    def loader(self,**constants):
        return r.from_url("redis://localhost:6379")

    # Used for talk with other Workers
    async def speak(self,**constants):
        #async with worker.app.broker.pubsub() as pubsub:
            #await worker.app.broker.publish(key, value)
        #asyncio.get_running_loop().create_task(worker.app.broker.publish(key, value))
        for key in constants['keys']:
            await constants['app'].broker.publish(key, constants['value'])
        #await worker.app.broker.xadd(key, {'message': value},maxlen=10)
        #b = await worker.app.broker.xlen(key)
        #print(b)

    async def hear(self,**constants):
        async def reader(channel):
            while True:
                await asyncio.sleep(0.01)
                print("########")
                message = await channel.get_message(ignore_subscribe_messages=True)
                if message is not None:
                    print(f"--------------------------------------(Reader) Message Received: {message}")
                    if message["data"].decode() == 'stop':
                        print("(Reader) STOP")
                        break
                    

        async with constants['app'].broker.pubsub() as pubsub:
            await pubsub.psubscribe(*constants['keys'])
            #if coroutine == None:
            #await pubsub.subscribe(**coroutine)
            future = asyncio.create_task(reader(pubsub))
            await future
            #await pubsub.psubscribe("tokens")

    async def signal(self,**constants):
        for key in constants['keys']:
            #await constants['app'].broker.publish(key, constants['value'])
            #await constants['app'].broker.xadd(key,{ 'v': constants['value'] })
            await self.connection.xadd(key,{ 'v': constants['value'] })
        
        #print( f"stream '{sname}' length: {r.xlen( stream_key )}")

    async def react(self,**constants):
        while True:
            await asyncio.sleep(0.1)
            l = await self.connection.xread(count=1, streams={constants['keys'][0]:0} )
            if len(l) != 0:
                #print(l)
                #await constants['app'].broker.xack(constants['keys'][0],'',l[0][1][0][0])
                await self.connection.xdel(constants['keys'][0],l[0][1][0][0])
                print(f"--------------------------------------(Reader) Message Received: {l[0][1][0][0]}:{l[0][1][0][1]}")