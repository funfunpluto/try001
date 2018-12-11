#! /usr/local/bin/python3


fname = 'ignorefiles/names'
text = open(fname, 'r').read()
members = text.split(';;')

cleanN = []
cleanE = []
for mem in members:
    mem = mem.strip()
    mem = mem.replace('&gt','')
    
    mem = mem.split('&lt;')
    #print(mem)
    name = mem[0].strip()
    name = name.replace('\n','')
    email = mem[1]
    
    if name not in cleanN:
        cleanN.append(name)
        cleanE.append(email)
for i in range(len(cleanN)): 
    item = "\"%s\" <%s>" %(cleanN[i], cleanE[i])
    print(item)
