def XML(worker,target):
    return dicttoxml.dicttoxml(asdict(target), attr_type=False).decode()