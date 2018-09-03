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


def most_frequent_words(n,massive_text):
    #word_freq = [[word_1,frequency_1],[word_2,frequency_2],...]
    seen,word_freq,occurrences = [],[],[]
    words = massive_text.split(" ")
    for word in words:
        word = word.replace(".","")
        if word not in seen:
            seen.append(word)
            occurrences.append(1)
        else:
            occurrences[seen.index(word)] = occurrences[seen.index(word)] + 1
    for k in range(0,len(occurrences)):
        word_freq.append([occurrences[k],seen[k]])
    word_freq.sort()
    word_freq.reverse()
    return word_freq[:n]

in_file = file_read("text.txt")

massive_text = """ """
massive_text.replace("\n","")

for element in in_file:
    massive_text = massive_text + element

print(most_frequent_words(10,massive_text))
