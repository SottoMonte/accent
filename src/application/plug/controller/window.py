import application.usecases.flow as flow
import flet as ft
import inspect

@flow.async_function(wait='start',act=('echo',),ports=('presentation','filesystem'))
async def open_window(e,**constants):
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