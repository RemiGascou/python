def ic(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz" #On crée un string contenant l'alphabet
    alphabet = alphabet .upper()            #On le passe en majuscules
    ic = 0                                  #On pose une variable ic qui va contenir l'IC
    for k in range(0,len(alphabet)):        #On itère sur l'alphabet pour faire la somme des counts
        fi = text.count(alphabet[k])        #On compte le nombre d'occurences de la lettre dans le texte
        ic = ic + fi*(fi-1)                 #On rajoute le cout à ic
    N = len(text)                           #N = la longueur du texte
    ic = ic/(N*(N-1))                       #On divise par la longueur du texte
    return ic



def coincidence_index(text):
    """
    Index of Coincidence
    
    The index of coincidence is a measure of how similar a frequency distribution is to the uniform distribution.
    The I.C. of a piece of text does not change if the text is enciphered with a substitution cipher.
    """
    return sum([text.count("abcdefghijklmnopqrstuvwxyz".upper()[k])*(text.count("abcdefghijklmnopqrstuvwxyz".upper()[k])-1) for k in range(0,len("abcdefghijklmnopqrstuvwxyz".upper()))])/(len(text)*(len(text)-1))
    

e = """PUMWMCBEYNCCPKOGCLTHPORLDCMDETCTGCIYPEZKRRPHJTWAEENNCCPKIOYDGHVMEESETLSEDEAODATSPQAKICLWPYIELLEIDSUTYZXIUENETGACKEJDEPLBLTNOEPANOLTRZVAEPOEPUNWTOEJYMXPXRZCKPJELXORTELMJTHLEVECYOYZREBEYEZFOKHEYNVYGTAYOHETRYAEIATHKPJTEIFOCXWALNIBFIFLNCETSNKHEAFFLZCKPJMSLSEOESEECRJAXAEDTSPTRZVAEPOEPISFDIDKODPNVYGTIETWCFMPFEETZONLWPYZNFPLWISLEEZGODPUEPXHVPRTGETVKEJMESVDOYELEGUBWTGKVYBPNEUJEOQELIJPUMWMCBEYDNENSEFCPILPSHLCIDRLLZHMNXUSPCWAEEADJENUCOYGINZENEXITYODQZVEECRJAXIEGCZYXEETAYOZEIIFJTRGUIGTEELJIGYLXUIESLYHPIIVLEIKVYSNLRBVKEAEWETREEPRSLRIYRSNCYTSPSWEERDZJTYEPCTZAKEKPJWCRNDPNVYGTCZYXEETAYOGRVATPOMGZTAWDMGEATFCI"""

print(ic(e))