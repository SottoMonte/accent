def set(worker,target,value):
    if hasattr(value,'__iter__'):
        return Metadata(target.typee,value,target.identifier,len(value),target.required)
    elif value == None:
        return Metadata(target.typee,value,target.identifier,0,target.required)
    else:
        return Metadata(target.typee,value,target.identifier,1,target.required)