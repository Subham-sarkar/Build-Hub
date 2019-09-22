fl=open('test.txt','w')

fl.seek(1000*1000)
fl.write('#')

fl.close()
