def STRING(worker,target):
    return f"<{target.required}> {target.typee:<15.15}:{target.identifier:<25.25} := {target.cardinality}:{target.value}"