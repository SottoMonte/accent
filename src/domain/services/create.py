
def Worker(app,job):
    return WORKER(f"{app.identifier}.{job.__name__}",job,dict({}),app,[])