class IntegerAnalysis():
    def __init__(self,n):
        self.n = n
    
    ## sign
    def sign(self):
        if self.n >= 0 :
            return "+"
        else :
            return "-"
    ## prime_factors
    def prime_factors(n):
        factors = []
        for k in range(2,n+2):
            while n % k == 0:
                factors.append(k)
                n = n//k
        return factors
    ## isPrime
    def isPrime(self):
        if self.n <= 1 :
            return False
        else :
            for k in range(2,int(self.n**(0.5)+1)):
                if self.n % k == 0:
                    return False
            return True
    ## fullAnalysis
    def fullAnalysis(self,verbose = False):
        # Data structure : list analysis
        # [sign,isPrime,prime_factors]
        def sign():
            if self.n >= 0 :
                return "+"
            else :
                return "-"
        def isPrime():
            if self.n <= 1 :
                return False
            else :
                for k in range(2,int(self.n**(0.5)+1)):
                    if self.n % k == 0:
                        return False
                return True
        def prime_factors():
            p = abs(self.n)
            factors = []
            for k in range(2,p+2):
                while p % k == 0:
                    factors.append(k)
                    p = p//k
            return factors
        analysis = [sign(),isPrime(),prime_factors()]
        
        if verbose == True:
            print("◘ Analysis of integer",x)
            print("|   Sign :",analysis[0])
            print("|   Prime :",analysis[1])
            print("|   Prime factors :",analysis[2])
            
        return analysis
        
        
x = -10  
ia = IntegerAnalysis(x)
ia.fullAnalysis(True)
#print(ia.fullAnalysis(True))
