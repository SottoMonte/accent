import application.usecases.flow as flow
import flet as ft
import inspect

@flow.async_function(ports=('presentation',))
async def plus_click(e,**constants):
    box = constants['presentation'].tree_view['box']
    box.value = str(int(box.value) + 1)
    await e.page.update_async()