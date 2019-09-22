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
def First():
    
    os.chdir('files')
    l = list()
    l2 = list()
    f = open('Name.txt')
    #data = f.read()
   
    for line in f:
        #print(line)
        key, author = line.split('|')
        ext = fext(key)
        l2 = [key, author, ext]
        l.append(l2)

    f.close()   
    os.chdir('./..')
    
    return l
    
    
