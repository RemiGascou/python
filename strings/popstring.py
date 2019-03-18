def popheadstr(s, k):
    return s[k:],s[:k] 

def popqueuestr(s, k):
    return s[:-k],s[-k:] 

data = "abcdefghijklmnopqrstuvwxyz"

for k in range(len(data)//2):
    data, t = popqueuestr(data, 2)
    print(t, data)