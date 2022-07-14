def destCity(paths):
    adj_obj = {}
    
    for path in paths:
        adj_obj[path[0]] = path[1]
        
    for dest in adj_obj.values():
        if not dest in adj_obj:
            return dest
        else:
            continue
    return dest