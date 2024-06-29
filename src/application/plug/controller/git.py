import application.usecases.flow as flow
import flet as ft

@flow.async_function(wait='start',act=('echo',),ports=('presentation','persistence'))
async def open_file(e,**constants):
    testo = await constants['persistence'].read(file=e.control.tooltip)
    win = await constants['persistence'].read(file='/home/asd/accent/src/domain/views/layout/window.xml')
    vista = await constants['persistence'].read(file='/home/asd/accent/src/domain/views/tab.xml')
    vista = vista.replace("@file_name", e.control.text)
    win = win.replace("@Title", e.control.tooltip)
    #print(vista,testo)
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
    print(win)
    view = await constants['presentation'].builder('n',win)
    constants['presentation'].tree_view['slave'].controls.append(view)

    await e.page.update_async()

@flow.async_function(ports=('presentation','persistence'))
async def work_path(e,**constants):
    #print(constants)
    fs = await constants['persistence'].tree(path='/home/asd/accent')

    def builder(data,depth=0,path=''):
        tot = []
        if 'dir' in data:
            for x in data[3]:
                print(x)
                tot.append(builder(x,depth+1))
                    
            aa = ft.Column(
                    controls=tot,
                    spacing=0
                )

            pb = ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(icon=ft.icons.POWER_INPUT, text="Check power"),
                ],

            )

            cc = ft.Column(
                    controls=[ft.TextButton(text=data[1],on_long_press=open_file),aa],
                    spacing=0
                )

            vv = ft.Container(
                    content=cc,
                    #padding=ft.padding.only(left=10),
                )
            return vv
        else:
            return ft.TextButton(text=data[2],on_long_press=open_file,tooltip=data[1])

    print(fs)
    a = builder(fs[0])
    constants['presentation'].tree_view['contesto'].content = ft.ListView(
                    controls=[a],
                    spacing=0,
                )
    
    await e.page.update_async()

@flow.async_function(ports=('presentation','persistence'))
async def work_area(e,**constants):
    #print(constants)
    fs = await constants['persistence'].tree(path='/home/asd/accent')
    vista = await constants['persistence'].read(file='/home/asd/accent/src/domain/views/directory.xml')

    async def builder(data,depth=0,path=''):
        tot = []
        if 'dir' in data:
            for x in data[3]:
                print(x)
                tot.append(builder(x,depth+1))
                    
            
            return vv
        else:
            return ft.TextButton(text=data[2],on_long_press=open_file,tooltip=data[1])

    print(fs[0])
    view = await constants['presentation'].builder('n',vista,fs)
    constants['presentation'].tree_view['contesto'].content = view
    #constants['presentation'].tree_view['contesto'].content = await builder(fs)
    
    await e.page.update_async()

@flow.async_function()
async def isset(e,**constants):
    #g = await constants['console'].exe('ls')

    print(g)
    # git -C /home/asd/accent rev-parse
    await e.page.update_async()