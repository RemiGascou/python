def round1(f):
    if f - int(f) == 0:
        return f
    else:
        if abs(int(f) - f) < 0.5:
            return int(int(f))
        else:
            return int(int(f)+(f/abs(f)))

liste_fracs = [[-11,3],[400,5],[5,400],[7,99],[978,979]]

for d in liste_fracs :
    print(round1(d[0]/d[1]),round(d[0]/d[1]))