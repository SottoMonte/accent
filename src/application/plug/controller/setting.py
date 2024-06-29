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

@flow.async_function(ports=('presentation',))
async def bar_state_update(e,**constants):
    constants['presentation'].tree_view['extension'].value = "PYTHON"
    
    await e.page.update_async()

@flow.async_function(ports=('presentation','persistence'))
async def show(e,**constants):
    vista = await constants['persistence'].read(file='/home/asd/accent/src/infrastructure/views/property/container.xml')
    #vista = vista.replace("@SubTitle", str(type(e.control)))
    

    view = await constants['presentation'].builder('n',vista)
    constants['presentation'].tree_view['property'].content = view
    await e.page.update_async()


async def close_window(e):
    await e.page.window_destroy_async()

async def minimize_window(e):
    e.page.window_maximized()