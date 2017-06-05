def nub2(inpt):
    
 
def nub1(inpt):
    nv = []
    [nv.append(item) for item in inpt if not item in nv]
    return nv

def list_remove_doubles(liste):
    seen = set()
    out = []
    for item in liste:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out
