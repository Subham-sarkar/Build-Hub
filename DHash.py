import os

def fold(s,l):
    if s == '':
        return
    a = s[0:3]
    s = s[3:]
    l.append(a)
    fold(s,l)


def threeHash(l):
    hashList = list()
    for s in l:
        hashString = ''.join(str(ord(c)) for c in s)
        hashList.append(int(hashString))
    return hashList

def add(l):
    summation = int()
    fileSize = 1000
    i=1
    while(i < len(l)):
            summation = (summation + (l[i] + l[i-1]))%fileSize
            i = i+2
    if((len(l) % 2) != 0):
        summation = (summation + l[-1])%fileSize 
    return summation


def Hash(s):
    l = list()
    fold(s,l)
    b = threeHash(l)
    c = add(b)    
    l.clear()
    return c

def hash_Two(key):
    length = len(key)
    mid = int(length/2)
    l = mid-1
    r = mid+1
    nw_key = key[l:r+1]
    list1 = list()
    list1.append(nw_key)
    list2 = threeHash(list1)
    nw_hash_id = add(list2)
    return nw_hash_id




def prepare(st):
    #st = '{'+st
    while len(st) < 1000:
        st += " "
    
    return st

def collision(file, pos):
    file.seek(pos)
    st = file.read(1)
    #print(st)
    #print(st.isalpha())
    return st.isalpha()




def makeHash(key, data, author):
    #key = "lowerisso"
    #data = "This is me "
    os.chdir('files')
    f = open('Name.txt','a')
    f.write(key+'|'+author+'\n')
    f.close()
    data = author+'%$%'+key+'%$%'+data
    data = prepare(data)

    #print(key)
    address = Hash(key)
    #print(address)
    address *= 1000
    file = open('Data.txt','r+')
    offset = hash_Two(key)
    offset *= 1000
    #print(address)
    #print(offset)
    count = 0
    while collision(file,address) :
        count += 1
        address = (address + offset)%1000000

    #print("Collossion for "+str(count))
    #print(int(address/1000))
    file.seek(address)
    file.write(data)
    file.close()

    os.chdir('./..')
    #file.close()
    return count

def found(key, author):
    os.chdir('files')
    f = open('Name.txt')
    flag = 0
    key = key.strip()
    for line in f:
        
        line = line.strip()
        #print(line)
        pgm, name = line.split('|')
        #print(key,pgm,author,name)
        #print(pgm)
        if author == name and key == pgm:
            flag = 1
            break
    
    f.close()
    os.chdir('./..')
    if flag == 0:
        return False
    else:
        return True

    


def findHash(key,author):
    address = Hash(key)
    address *= 1000
    if(not found(key, author)):
        return False
    os.chdir('files')

    file = open('Data.txt','r+')
    #print(address)
    while True:
        file.seek(address,0)
        

        
        l = file.read(1000)
        if not l:
            file.close()
            os.chdir('./..')
            return False
        a = list()
        a = l.split('%$%')
        #print(a)
        
        if a[0] == author:
            if a[1] == key:
                file.close()
                os.chdir('./..')
                return a[2]
                    
        address += (hash_Two(key)*1000)
            
        

        
