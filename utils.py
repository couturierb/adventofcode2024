def flat_map_recursive(liste) :
    if not type(liste) is list :
        return liste
    
    result = []
    for elem in liste :
        if type(elem) is list :
            result += flat_map_recursive(elem)
        else :
            result.append(elem)
    return result
