import string

def compress(string):

    res = ""

    count = 1

    #Add in first character
    res += string[0]

    #Iterate through loop, skipping last one
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                #Ignore if no repeats
                res += str(count)
            res += string[i+1]
            count = 1
    #print last one
    if(count > 1):
        res += str(count)

    nres = res.replace('\n','\\n')
    return nres



def decompress(string):
    char_holder = ''
    decompressed_out = ''
    for char in string:
        if char.isalpha():
            char_holder = char
            decompressed_out += char_holder
        elif char.isdigit():
            char = int(char)
            if char_holder != '':
                decompressed_out += (char-1) * char_holder

            else:
                decompressed_out += str(char)
            char_holder = ''
        else:
            
            decompressed_out += char

    #nres = decompressed_out.replace('\\n','\n')

    return decompressed_out
