##Square Root Approximation
def sra_heron(X,n):
    r = 1
    for k in range(n):
        d = X / r
        r = (r + d)/2
    return round(r,7)
    
print(sra_heron(10,3))