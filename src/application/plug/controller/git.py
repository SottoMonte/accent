import application.usecases.flow as flow

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