
def faili_lugemine(f):

    while True :
        jook.append(f.readline().strip().split('.  ')[1:])
        retsept.append(f.readline().strip().strip()[:])
        f.readline()
        kirjeldus.append(f.readline().strip().strip()[:])
        f.readline()
        pilt.append(f.readline().strip().strip()[:])
        
        if f.readline() == '':
            break
    


def retsepti(jook, retsept, kirjeldus, pilt):
    a = ()
    b = ()
    for i in range(len(jook)):
        retseptid[jook[i][0]] = [(retsept[i])]
        
        retseptid[jook[i][0]] += [(kirjeldus[i])]
        retseptid[jook[i][0]] += [(pilt[i])]

    
def sisendi_otsimine(sisend):#listina
    
    valitud_joogid = []
    

    for võti, sisu in retseptid.items():
        for osa in sisend:
            if osa in sisu[0]:
                valitud_joogid.append(võti)
                
    sobilikud_joogid = set(valitud_joogid)
    
    lõplikud_joogid = []
    for jook in sobilikud_joogid:
        if len(sisend) == valitud_joogid.count(jook):
            lõplikud_joogid.append(jook)
    
    for jook in lõplikud_joogid:
        print(jook)
        print(retseptid[jook][0])
        print(retseptid[jook][1])
                

f = open('info.txt', encoding = 'utf-8')
retseptid = {}
jook = []
retsept = []
kirjeldus = []
pilt = []


faili_lugemine(f)

retsepti(jook, retsept, kirjeldus, pilt)

sisendi_otsimine(['Rum', 'Mint'])

f.close()