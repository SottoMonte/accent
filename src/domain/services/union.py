def UNION(worker,target,value):
    if hasattr(target.value,'__iter__'):
        return SET(worker,target,target.value + value)
    else:
        return SET(worker,target,target.value + value)