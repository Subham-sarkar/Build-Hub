import os
import re

def search_language(ext):
    os.chdir('files')
    f1 = open('Name.txt')
    namel= list()
    flag=0
    for l in f1:
        a, b=l.split('|')
        exte=a.split('.')
        extension = exte[-1]
        if extension == ext:
            name = a
            author = b
            namel.append([name,author,ext])
            flag =1
    if flag==1:
        f1.close()
        os.chdir('./..')
        return namel
    else:
        f1.close()
        os.chdir('./..')
        return 0
        


