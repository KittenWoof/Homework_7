from encodings import utf_8
import fnmatch
import os
import io
from operator import itemgetter

def parce_file(file):
    item_file = []
    with io.open(entry, 'r', encoding = 'utf_8') as file:          
        lines = file.readlines()
        item_file.append(entry)
        item_file.append(len(lines))
        item_file.append(lines)
        file.close
    return item_file

list_files = []

list_of_files = os.listdir('.')  
pattern = "*.txt"  
for entry in list_of_files:  
    if fnmatch.fnmatch(entry, pattern):
        list_files.append(parce_file(entry))
        
sort_list = sorted(list_files, key=itemgetter(1), reverse=False)

f = open('cool.txt', 'w', encoding='utf_8')

for item in sort_list:
    for i in range(len(item)):
        if i == 0 or i == 1:
            f.write(f"{item[i]}\n")
        else:
            for str in item[i]:
                f.write(str.rstrip() + '\n')

print(list_files)
print(sort_list)