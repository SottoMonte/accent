# Import
import sys

import domain.enums.application as APP
from application.usecases import run,flow

#@flow.async_function(at='12:05',wait='start',act=('echo',))
@flow.async_function(at='20:35',wait='start',act=('echo',))
async def wrkr1(**constants):
    #metadata = importlib.import_module('domain.entities.metadata', package=None)
    #await redis.adapter.create(app=zt,data=metadata.metadata('string','ciao','somma',1,None,zt))
    #aaa = await redis.adapter.read(app=zt,id='somma')
    print("====>",'LAVORO IN CORSO -----------------------------------',constants['application'].args)

# main
if __name__ == "__main__":
    run.application(identifier='hub.cloud',args=sys.argv,interfaces={APP.INTERFACE.GUI:None},workers={wrkr1})