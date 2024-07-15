import application.usecases.flow as flow
import flet as ft

@flow.async_function(wait='start',act=('echo',),ports=('presentation','persistence'))
async def open_file(e,**constants):
    testo = await constants['persistence'].read(file=e.control.tooltip)
    #win = await constants['persistence'].read(file='/home/asd/accent/src/domain/views/layout/window.xml')
    #vista = await constants['persistence'].read(file='/home/asd/accent/src/domain/views/tab.xml')
    '''vista = vista.replace("@file_name", e.control.text)
    win = win.replace("@Title", e.control.tooltip)
    print(vista,testo)
    vista = vista.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
    testo = testo.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
    if e.control.text.endswith(".xml"):
        
        vista = vista.replace("@extede", e.control.tooltip)
        vista = vista.replace("@file", testo)
        win = win.replace('<Import view="@extede" />', vista)
        
        #view = await constants['presentation'].builder('n',testo)
        #constants['presentation'].tree_view['previw'].content = view
        pass
    else:
        vista = vista.replace("@file", testo)
        win = win.replace('<Import view="@extede" />', vista)
    print(win)'''
    view = await constants['presentation'].builder('n','src/domain/views/layout/window.xml',{'window':e.control.text,'file':testo})
    
    constants['presentation'].tree_view['slave'].controls.append(view)

    await e.page.update_async()

@flow.async_function(ports=('presentation','persistence'))
async def work_path(e,**constants):
    #print(constants)
    #fs = await constants['persistence'].tree(path='/home/asd/accent')


    #print(fs)
    #a = builder(fs[0])
    #constants['presentation'].tree_view['contesto'].content = ft.Text("TEST")
    
    await e.page.update_async()

@flow.async_function(ports=('presentation','persistence'))
async def work_area(e,**constants):

    fs = await constants['persistence'].tree(path='/home/asd/accent')
    
    view = await constants['presentation'].builder('n','src/domain/views/directory.xml',{'users':[('src/application/plug/controller/git.py','/home/asd/accent/src/application/plug/controller/git.py'),('/a/b','file.txt')]})
    constants['presentation'].tree_view['contesto'].content = view
    
    await e.page.update_async()

@flow.async_function()
async def isset(e,**constants):
    #g = await constants['console'].exe('ls')

    print(g)
    # git -C /home/asd/accent rev-parse
    await e.page.update_async()