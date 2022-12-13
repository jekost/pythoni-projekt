
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
        test = []
        for osa in sisend:
            if osa in sisu:
                test.append(osa)
                #if sisu == test:
                #    valitud_joogid.append(võti)
                if set(sisu).issubset(test):
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
#print(sisendi_otsimine(['Tequila', 'White Rum', 'Sugar Syrup', 'Lime Juice', 'Dry Vermouth', 'Gin', 'Sugar']))
#print(sisendi_otsimine(['Tequila', 'White Rum', 'Sugar Syrup', 'Lime Juice', 'Dry Vermouth', 'Gin', 'Sugar']))

pildi_nimed = {'Mojito': 'Mojito1.jpg', 'Martini': 'Martini1.jpg', 'Daiquiri': 'Daiquiri.jpg', 'Old Fashioned': 'Untitled-2.jpg', 'Cosmopolitan': 'Cosmopolitan-1.jpg', 'Caipirinha': 'Caipirinha1.jpg', 'White Russian': 'White-Russian.jpg', 'Pina Colada': 'Pina-Colada.jpg', 'Negroni': 'Negroni.jpg', 'Bramble': 'Bramble.jpg', 'Margarita': 'Margarita-206x300.jpg', 'Dark `N` Stormy': 'Dark-n-Stormy-200x300.jpg', 'Cuba Libre': 'Cuba-Libre.jpg', 'Sazerac': 'Sazerac.jpg', 'Bloody Mary': 'Bloody-Mary1.jpg', 'Manhattan': 'Manhattan.jpg', 'Long Island Iced Tea': 'Long-Island-Iced-Tea-1.jpg', 'Mai-Tai': 'Mai-Tai-2.jpg', 'Amaretto Sour': 'Amaretto-Sour-200x300.jpg', 'Singapore Sling': 'Singapore-Sling2.jpg', 'French Martini': 'French-Martini-1.jpg', 'Espresso Martini': 'Espresso-Martini.jpg', 'Strawberry Daiquiri': 'Strawberry-Daiquiri.jpg', 'Moscow Mule': 'Moscow-Mule-1.jpg', 'Clover Club': 'clover-club-cocktail.jpg', 'Mint Julep': 'Mint-Julep.jpg', 'John Collins': 'Jock-Collins.jpg', 'Gin Sour': 'Gin-Sour.jpg', 'Appletini': 'Appletini.jpg', 'White Lady': 'White-Lady.jpg', 'Black Russian': 'Black-Russian.jpg', 'Brandy Alexander': 'Brandy-Alexander-2.jpg', 'French 75': 'French-75-cocktail.jpg', 'Navy Grog': 'Navy-Grog-2.jpg', 'Rusty Nail': 'Rusty-Nail1.jpg', 'Pisco Sour': 'Pisco-Sour.jpg', 'Bucks Fizz': 'Bucks-Fizz1.jpg', 'Rum Runner': 'Rum-Runner.jpg', 'El Presidente': 'El-Presidente.jpg', 'WooWoo': 'WooWoo-200x300.jpg', 'Kir Royale': 'Kir-Royale1.jpg', 'Bellini': 'Bellini1.jpg', 'Lemon Drop Martini': 'Lemon-Drop-Martini.jpg', 'Pink Gin': 'Pink-Gin.jpg', 'Salty Dog': 'salty-dog-recipe-1.jpg', 'B-52': 'B-52.jpg', 'Painkiller': 'Pain-Killer-2.jpg', 'Screwdriver': 'Screwdriver-1.jpg', 'French Connection': 'French-Connection.jpg', 'Paloma': 'Paloma.jpg', 'Royal Hawaiian': 'Royal-Hawaiin-2.jpg', 'Tommy`s Margarita': 'Tommys-Margarita-2.jpg', 'Sea Breeze': 'Sea-Breeze-1.jpg', 'Ramos Gin Fizz': 'Ramos-Gin-Fizz.jpg', 'El Diablo': 'El-Diablo.jpg', 'Breakfast Martini': 'Breakfast-Martini.jpg', 'Caipivodka': 'Caipivodka.jpg', 'Baja Gold': 'Baja-Gold-2.jpg', 'Sex on the Beach': 'sex-on-the-beach-cocktail-recipe.jpg', 'Tequila Sunrise': 'Tequila-Sunrise.jpg', 'Bronx': 'Bronx.jpg', 'Caribbean Sunrise': 'Caribbean-Sunrise.jpg', 'Gibson': 'Gibson.jpg', 'Bay Breeze': 'Bay-Breeze.jpg', 'Raspberry Mojito': 'Raspberry-Mojito1.jpg', 'SideCar': 'Sidecar.jpg', 'Champagne Cocktail': 'Champagne-Cocktail.jpg', 'Godfather': 'Godfather.jpg', 'Hemingway Daiquiri': 'Hemmingway-Daiquiri.jpg', 'Raspberry Daiquiri': 'Raspberry-Daiquiri.jpg', 'Blueberry Collins': 'Blueberry-Collins.jpg', 'Gimlet': 'Gimlet.jpg', 'Chocolate-covered Cherry': 'Chocolate-Covered-Cherry.jpg', 'Lemongrad': 'Lemongrad.jpg', 'Planters Punch': 'Detropolitan.jpg', 'Blushing Bride': 'Blushing-Bride.jpg', 'Gin Rickey': 'Gin-Ricky.jpg', 'Passion Fruit Daiquiri': 'Passion-Fruit-Daiquiri.jpg', 'Cantarito': 'Cantarito.jpg', 'Brandy Collins': 'Brandy-Collins.jpg', 'Volcano': 'Volcano-2.jpg', 'Americano': 'Americano-2.jpg', 'Accomplice': 'Accomplice.jpg', 'Berry Nice': 'Berry-Nice.jpg', 'Mojito Royal': 'Mojito-Royal.jpg', 'Tom Collins': 'Tom-Collins1.jpg', 'Blackberry Mule': 'Blackberry-Mule.jpg', 'Toasted Almond': 'Toasted-Almond.jpg', 'Boston Sour': 'Boston-Sour.jpg', 'Detropolitan': 'Planters-Punch.jpg', 'Alaska Cocktail': 'Alaska-Cockatil.jpg', 'Cheeky Vimto': 'Cheeky-Vimto.jpg', 'Amaretto Sunrise': 'Amaretto-Sunrise.jpg', 'Ballet Ruse': 'Ballet-Ruse.jpg', 'Beachcomber': 'Beachcomber.jpg', 'Blind Russian': 'Blind-Russian.jpg', 'Midori Sour': 'sour.jpg', 'Donald Sutherland': 'Donald-Sutherland.jpg', 'Southside': 'Southside.jpg', 'Wahine': 'Wahine-2.jpg'}

