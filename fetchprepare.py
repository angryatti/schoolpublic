from array import array
#import json
import random


rendabc = list(map(chr, range(ord('A'), ord('Z')+1)))
arrayofabc = list()

print("Random rendszám generátor v5:")
classice = int(input("Válaszon 1) klasszikus rendszám 2) Új rendszám"))
db = int(input("Hány darabot szeretne?"))

def negyvagy3(classice, db):
    abc = ""
    for j in range(db):
        if (classice==2):
            for i in range(4):
                valami = random.randrange(0,25)
                if (i==2):
                    abc+=" "
                abc = abc+rendabc[valami]
            valami = random.randrange(-1,999)+1
            abc = abc+"-"+str(valami).zfill(3)
            if abc not in arrayofabc:
                arrayofabc.append(abc)
            abc=""
        else:
            for i in range(3):
                valami = random.randrange(0,25)
                abc = abc+rendabc[valami]
            valami = random.randrange(-1,999)+1
            abc = abc+"-"+str(valami).zfill(3)
            if abc not in arrayofabc:
                arrayofabc.append(abc)
            abc=""            



# ennyi rendszámot generál
if (classice==1):
    negyvagy3(1,db)
else:
    negyvagy3(2,db)
    # 4-betű tartalmaz
   

# fájlba írás 
with open('rendszamok.json','w',encoding='utf-8') as kifile:
    kifile.write('[')
    for o in range(0,len(arrayofabc),1):
        if o!=len(arrayofabc)-1:
           kifile.write('{"rendsz": "'+arrayofabc[o]+'"},')
        else:
            kifile.write('{"rendsz": "'+arrayofabc[o]+'"}')
    
        
    kifile.write(']')
        
print("A fájlba írás megtörtént")

#json_dumps = json.dumps(arrayofabc)


#print("{"+json_dumps+"}")