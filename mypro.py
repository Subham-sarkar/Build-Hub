import os
lookup = {
        'c':'C',
        'py':'Python',
        'java':'Java',
        'pl':'Perl',
        'cpp':'C++',
        'net':'.NET',
        'txt':'Text',
        'js':'java Script',
        'html':'Html',
        'css':'CSS',
        'php':'PHP',
        'm':'Objective C',
        'cs':'C#',
        'vb':'Visual Basic'
        }

def fext(s):
    name,ext = s.split('.')
    try:
        return lookup[ext]
    except:
        return ext
def mypro(author):
    #print(author)
    os.chdir('files')
    l = list()
    b = list()
    f = open('Name.txt','r')
    for line in f:
        #print(line)
        key, fauthor = line.split('|')
        fauthor = fauthor.strip()
        #print(key,fauthor)
        #print(author)
        if author == fauthor:
            #print(True)
            b = [key, author, fext(key)]
            #print(b)
            l.append(b)
    
    f.close()

    os.chdir('./..')
    return l
