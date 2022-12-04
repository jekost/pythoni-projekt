
# loeb info listidesse 
def faili_lugemine():
    f = open('info.txt', encoding = 'utf-8')

    while True :
        jook.append(f.readline().strip().split('.  ')[1:])
        retsept.append(f.readline().strip().strip()[:])
        f.readline()
        kirjeldus.append(f.readline().strip().strip()[:])
        f.readline()
        pilt.append(f.readline().strip().strip()[:])
        
        if f.readline() == '':
            f.close()
            break
    
    

# lisab sõnastikku joogi nime järgi retsepti, kirjelduse ja pildi
def retsepti(jook, retsept, kirjeldus, pilt):
    for i in range(len(jook)):
        retseptid[jook[i][0]] = [(retsept[i])]
        
        retseptid[jook[i][0]] += [(kirjeldus[i])]
        retseptid[jook[i][0]] += [(pilt[i])]

    
def sisendi_otsimine(sisend):#listina
    
    valitud_joogid = []
    

    for võti, sisu in retseptid_otsing.items():
        muutuja = sisu
        for osa in sisend:
            if osa in muutuja:
                muutuja.remove(osa)
                if muutuja == []:
                    valitud_joogid.append(võti)
                
    return valitud_joogid

# valitud joogi väljastmaiseks  
def joogiväljund(jook):
    return retseptid[jook]


# otsib olulisemad joogid listidest ja tagastab nende listi
def koostis_osadenimi(retsept):
    ainult_vajalikud_koostisosad = []
    for i in range(len(retsept)):
        sisu_eraldi = retsept[i].split(',')
        
        for element in sisu_eraldi:
            if 'ml' in element:
                vajalik = element.split('ml ')
                if vajalik[1] not in ainult_vajalikud_koostisosad:
                    ainult_vajalikud_koostisosad.append(vajalik[1])
            
            if 'dashes of' in element:
                vajalik = element.split('dashes of ')
                if vajalik[1] not in ainult_vajalikud_koostisosad:
                    ainult_vajalikud_koostisosad.append(vajalik[1])
                else:
                    continue
            elif 'dashes'  in element:
                vajalik = element.split('dashes ')
                if vajalik[1] not in ainult_vajalikud_koostisosad:
                    ainult_vajalikud_koostisosad.append(vajalik[1])
                
            elif 'dash' in element:
                vajalik = element.split('dash ')
                if vajalik[1] not in ainult_vajalikud_koostisosad:
                    ainult_vajalikud_koostisosad.append(vajalik[1])
                     
    return ainult_vajalikud_koostisosad

def retseptid_otsinguks(retseptid, vajalikud_koostisosad):
    retseptid_otsing ={} 
    for võti, sisu in retseptid.items():
        list_elementidest = sisu_eraldi(sisu[0])
        retseptid_otsing[võti] = list_elementidest
    return retseptid_otsing

def sisu_eraldi(string):
    ainult_vajalikud_koostisosad = []
    järjend = string.split(',')
    for element in järjend:
        if 'ml' in element:
            vajalik = element.split('ml ')
            if vajalik[1] not in ainult_vajalikud_koostisosad:
                ainult_vajalikud_koostisosad.append(vajalik[1])
        
        if 'dashes of' in element:
            vajalik = element.split('dashes of ')
            if vajalik[1] not in ainult_vajalikud_koostisosad:
                ainult_vajalikud_koostisosad.append(vajalik[1])
            else:
                continue
        elif 'dashes'  in element:
            vajalik = element.split('dashes ')
            if vajalik[1] not in ainult_vajalikud_koostisosad:
                ainult_vajalikud_koostisosad.append(vajalik[1])
            
        elif 'dash' in element:
            vajalik = element.split('dash ')
            if vajalik[1] not in ainult_vajalikud_koostisosad:
                ainult_vajalikud_koostisosad.append(vajalik[1])
    return ainult_vajalikud_koostisosad

"""def anna_joogid():
    a=[]
    for el in jook:
        a.append(el[0])
    return a
"""              

# kogu sõnastik kus on kõik joogi kohta käiv info
retseptid = {}
jook = [] #Jookide nimed
retsept = [] # jookide retseptid listis
kirjeldus = [] # jookide kirjeldus listis
pilt = [] # jookide pildi url listis

# Loeb sisu failist
faili_lugemine()
#faili sisu teeb sõnastikuks
retsepti(jook, retsept, kirjeldus, pilt)

#joogid mis lähevad valiku võimalusse
vajalikud_koostisosad = koostis_osadenimi(retsept)

# siin on sõnastik kus on joogid ja nende otsinguks vaja minevad asjad
retseptid_otsing = retseptid_otsinguks(retseptid, vajalikud_koostisosad)


#joogiväljund('Mojito')
#print(sisendi_otsimine(['Tequila', 'White Rum', 'Sugar Syrup', 'Lime Juice', 'Dry Vermouth', 'Gin', 'Sugar']))




<<<<<<< HEAD
=======
print(sisendi_otsimine(['Tequila', 'White Rum', 'Sugar Syrup', 'Lime Juice', 'Dry Vermouth', 'Gin', ]))
>>>>>>> 92a6bb558211639ae7a872d054f8944c62293899
