#Factorielle python. 
from time import *
import matplotlib.pyplot as plt

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def factperso(n):
    fact = 1
    for a in range(1,n+1):
        fact = a * fact
    return fact


def max_recursion_depth(f, startingstep = 1):
    """This function return the maximum recursion depth for a given function f."""
    """/!\ Don't forget to disable verbose mode on your function as max_recursion_depth(f) is using multiples tries."""
    try :
        while startingstep > 0:
            f(startingstep)
            startingstep = startingstep + 1
    except(RuntimeError): #RuntimeError: maximum recursion depth exceeded in comparison
        print('For function : "',str(f.__name__),'" (',str(f),') :\nMaximum recursion depth reached at ', startingstep,".\nLast working recursion step : ",startingstep-1, sep="")

max_recursion_depth(fact,1)

#max_recursion_depth(addrecur)
def function_time_comparison(nbofvalues, precision, value=987):
    listyrecur = []
    listynorm = []
    listx = []
    
    for x in range(nbofvalues):
        listx.append(x)
    for z in range(nbofvalues):
        tic = clock()
        factperso(value)
        listynorm.append(int((clock() - tic)*10**precision)/10**precision)
        tic = clock()
        fact(value)
        listyrecur.append(int((clock() - tic)*10**precision)/10**precision)
    
    plt.plot(listx, listyrecur, color = 'green')
    plt.plot(listx, listynorm, color = 'blue')
    plt.plot([0,nbofvalues-1],[sum(listyrecur)/len(listyrecur), sum(listyrecur)/len(listyrecur)], color='lightgreen')
    plt.plot([0,nbofvalues-1],[sum(listynorm)/len(listynorm), sum(listynorm)/len(listynorm)], color='lightblue')
    
    plt.show()

#function_time_comparison(100, 9)