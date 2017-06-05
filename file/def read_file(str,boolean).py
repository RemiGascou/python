def file_read(path,log = False):
    if log == True:
        print("Opening file ",path,"...")
        f = open(path,'r')
        print("Reading file ",path,"...")
        lignes  = f.readlines()
        print("Closing file ",path,"...")
        f.close()
        print("Done !")
    else :
        f = open(path,'r')
        lignes  = f.readlines()
        f.close()
    return lignes


file_read("0-2001000.primes",True)
#file_read("0-2001000.primes",False)
