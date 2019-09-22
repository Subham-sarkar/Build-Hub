
def ret(author,name):
    f = open('t.txt','r+')
    f.seek(0)
    l = f.readline()
    #print(l)
    a = list()
    a = l.split('%$%')
    #print(a)
    if a[0] == author:
        if a[1] == name:
            return a[2]
    print('false')
    f.close()

