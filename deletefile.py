import os

def deletef(key, author):
    os.chdir('files')
    wdata = str()
    f = open('Name.txt','r')
    for line in f:
        #print(line)
        line = line.strip()
        pgm, writer = line.split('|')
        #print(pgm)
        if pgm == key and writer == author:
            continue
        else:
            wdata += pgm + '|' + writer +'\n'

    f.close()
    f = open('Name.txt','w')
    f.write(wdata)
    f.close()
    os.chdir('./..')
