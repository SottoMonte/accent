import asyncio

from domain.enums import application as ENUM
from application.usecases import flow,loader

loader.bootstrap_adapter()

@flow.function(entities=('application',), ports=('messenger','presentation'))
def application(**constants):
    app = constants['application'](constants['identifier'],constants['interfaces'],'s', '', constants['args'],[], "bbroker", 'none')

    #start event manager
    a = constants['messenger']
    asyncio.get_event_loop().create_task(a.react(app=app,keys='c'))
    


    # avvia i lavoratori
    for worker in constants['workers']:
        #lab = WORKER.MakeWorker(self,job)
        asyncio.get_event_loop().create_task(worker(application=app))

    try:
        # Avvia le interfacce del programma
        for key, interface in app.interfaces.items():
            match key:
                case ENUM.INTERFACE.CLI:
                    #self.JOB(interface)
                    pass
                case ENUM.INTERFACE.GUI:
                    #flutter.flutter(None)
                    #flutter.presentation.loader(None)
                    zz = constants['presentation']
                    zz.loader()
                    pass
                case ENUM.INTERFACE.API:
                    pass
                case _:
                    print(f"Errore generico non esiste nessuna interfaccia {key}")
        
        #asyncio.get_event_loop().run_forever()

    except Exception as e:
        e_type = type(e).__name__
        e_file = e.__traceback__.tb_frame.f_code.co_filename
        e_line = e.__traceback__.tb_lineno

        e_message = str(e)

        print(f'exception type: {e_type}')

        print(f'exception filename: {e_file}')

        print(f'exception line number: {e_line}')

        print(f'exception message: {e_message}')
    except KeyboardInterrupt:
        print("Ctrl + C")