import application.usecases.flow as flow
import flet as ft
import inspect

@flow.async_function(ports=('presentation',))
async def plus_click(e,**constants):
    box = constants['presentation'].tree_view['box']
    box.value = str(int(box.value) + 1)
    await e.page.update_async()

@flow.async_function(ports=('presentation',))
async def men_click(e,**constants):
    box = constants['presentation'].tree_view['box']
    box.value = str(int(box.value) - 1)
    await e.page.update_async()

@flow.async_function(wait='start',act=('echo',),ports=('presentation','filesystem'))
async def open_file(e,**constants):
    testo = await constants['filesystem'].read(file=e.control.tooltip)
    win = await constants['filesystem'].read(file='/home/asd/accent/src/infrastructure/view/layout/window.xml')
    vista = await constants['filesystem'].read(file='/home/asd/accent/src/infrastructure/view/tab.xml')
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

@flow.async_function(ports=('presentation','filesystem'))
async def bar_state_update(e,**constants):
    constants['presentation'].tree_view['extension'].value = "PYTHON"
    
    await e.page.update_async()

@flow.async_function(ports=('presentation','filesystem'))
async def show(e,**constants):
    vista = await constants['filesystem'].read(file='/home/asd/accent/src/infrastructure/views/property/container.xml')
    #vista = vista.replace("@SubTitle", str(type(e.control)))
    

    view = await constants['presentation'].builder('n',vista)
    constants['presentation'].tree_view['property'].content = view
    await e.page.update_async()

@flow.async_function(ports=('presentation','filesystem'))
async def work_path(e,**constants):
    #print(constants)
    fs = await constants['filesystem'].tree(path='/home/asd/accent')

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


@flow.async_function(ports=('presentation','filesystem'))
async def work_area(e,**constants):
    #print(constants)
    fs = await constants['filesystem'].tree(path='/home/asd/accent')
    vista = await constants['filesystem'].read(file='/home/asd/accent/src/infrastructure/view/directory.xml')

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

async def close_window(e):
    await e.page.window_destroy_async()

async def minimize_window(e):
    e.page.window_maximized()

@flow.async_function(wait='start',act=('echo',),ports=('presentation','filesystem'))
async def shift(e,**constants):
    #mast = constants['presentation'].tree_view['master'].controls[0]
    
    for idx,win in enumerate(constants['presentation'].tree_view['slave'].controls):
        
        if win.content.controls[0].controls[1].controls[0].uid == e.control.uid:
            swap = constants['presentation'].tree_view['master'].controls[0]
            constants['presentation'].tree_view['slave'].controls[idx] = swap
            constants['presentation'].tree_view['master'].controls[0] = win
    await e.page.update_async()

@flow.async_function(wait='start',act=('echo',),ports=('presentation','filesystem'))
async def remove(e,**constants):
    
    for idx,win in enumerate(constants['presentation'].tree_view['slave'].controls):
        if win.controls[0].content.controls[0].controls[1].controls[2].uid == e.control.uid:
            constants['presentation'].tree_view['slave'].controls.remove(win)
            
    
    await e.page.update_async()

@flow.async_function(wait='start',act=('echo',),ports=('presentation','filesystem'))
async def mini(e,**constants):
    
    for idx,win in enumerate(constants['presentation'].tree_view['slave'].controls):
        if win.controls[0].content.controls[0].controls[1].controls[1].uid == e.control.uid:
            if win.controls[1].visible:win.controls[1].visible = False
            else: win.controls[1].visible = True
            
    
    await e.page.update_async()