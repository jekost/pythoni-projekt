f = open('info.txt', encoding = 'utf-8')
retseptid = {}
jook = []
retsept = []
kirjeldus = []
pilt = []

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

    



faili_lugemine(f)

retsepti(jook, retsept, kirjeldus, pilt)
print(retseptid)
f.close()