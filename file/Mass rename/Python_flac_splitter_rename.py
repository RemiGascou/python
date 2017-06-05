import os,sys

path = "C:/Users/Admin/Desktop/Kno/Kno (CunninLynguists) - 2016 - Bones [FLAC]"
list_files = []
list_files_new = []
final = []

for file in os.listdir(path):
    if file.endswith(".flac"):
        list_files.append(file)

print(list_files)

for element in list_files:
    new = element[:2] + " -" + element[2:]
    list_files_new.append(new)
    
print(list_files_new)
#print(list_files)


for n in range(len(list_files_new)):
    src = path + "/" + list_files[n]
    dest = path + "/" + list_files_new[n]
    os.rename(src,dest)


#os.system("pause")