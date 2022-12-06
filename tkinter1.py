from luger import *
import urllib.request
from tkinter import *
from PIL import ImageTk, Image, ImageOps
import io


#FUNK MIS KÄIVATAKSE JUHUL KUI KASTI VAJUTATAKSE
def tagasta():
    i=0
    output=[]
    for kast in kastid:
        if kast.var.get()==1:
            try:
                output.append(vähem_koostisosi[i])
            except:
                output.append(koostisosad[i])
        i+=1

    for widget in vaheraam.winfo_children():
        widget.destroy()

    misJooki = Label(vaheraam, text="what are you feeling?", background="lavender")
    misJooki.grid(row=0,sticky="n")

    rida=1
    lb=Listbox(vaheraam,height=20)

    for jook in sisendi_otsimine(output):
        lb.insert(rida,jook)
        rida+=1

    lb.grid()

    lb.bind("<<ListboxSelect>>", lbValik)


pildid = []
def lbValik(synd):
    valik = synd.widget.curselection()
    if valik:
        index = valik[0]
        data = synd.widget.get(index)
        print()

        try:
            for widget in retseptiraam.winfo_children():
                widget.destroy()
        except:
            True

        for el in joogiväljund(data):
            print (el)

        joogikoostisosad = Label(retseptiraam, text="the ingredients necessary for your drink:", bg="lavender")
        joogikoostisosad.grid(column=3, row=0, sticky="nw")

        joogiretsept = Label(retseptiraam, text="the recipe for your drink:", bg="lavender")
        joogiretsept.grid(column=3, row=2, sticky="nw")

        #tee koostisosade list, mis läheb tkinteri aknasse
        prinditav_koostisosa=""
        for koostiosa in joogiväljund(data)[0].split(","):
            prinditav_koostisosa+="-"
            prinditav_koostisosa+=koostiosa.strip()
            prinditav_koostisosa+="\n"
        prinditav_koostisosa=prinditav_koostisosa.strip()

        #pane koostisosade list ja retsept tkinteri aknasse
        Label(retseptiraam,text=prinditav_koostisosa,wraplength=200,justify="left").grid(column=3,row=1,sticky="w")
        Label(retseptiraam,text=joogiväljund(data)[1],wraplength=200,justify="left").grid(column=3,row=3,sticky="w")

        #loe välja pilt formaadis, et see sobiks tkinterisse
        data = urllib.request.urlopen(joogiväljund(data)[2]).read()
        piltAlgne = Image.open(io.BytesIO(data))
        piltAlgne = ImageOps.contain(piltAlgne, (190, 6969))
        pilt = ImageTk.PhotoImage(piltAlgne)

        #pane pilt tkinteri aknasse
        Label(retseptiraam,text="",bg="lavender").grid(column=3,row=4)
        Label(retseptiraam,image=pilt).grid(column=3,row=5,sticky="w")

        #ilma selleta ei tööta....
        pildid.append(pilt)



    else:
        print("")



def tee_kastid_otsi():#teeb ainult need kastid kus on sõne sees ("u"->"Rum","Sugar")
    sõne=tk_name.get()
    rida = 2
    tulp=0
    global kastid
    global vähem_koostisosi
    kastid = {}
    vähem_koostisosi=[]
    for koostisosa in koostisosad:
        if sõne.lower() in koostisosa.lower():
            vähem_koostisosi.append(koostisosa)
            #nüüd on olemas väiksem list, {koostisosa:index, ko2:in2, ..}

    for koostisosa in range(len(vähem_koostisosi)):
        nimi = vähem_koostisosi[koostisosa]
        rida += 1
        current_var = IntVar()
        current_box = Checkbutton(raam, text=nimi, variable=current_var, background="lavender", command=tagasta)
        current_box.grid(row=rida,column=tulp, sticky=W)
        current_box.var = current_var
        kastid[current_box] = nimi
        if not tulp==1:
            if rida==24:
                tulp+=1
                rida=0


#iga kord kui tekstikasti midagi kirjutatakse, kustutatakse kõik checkboxid ära
#ja tehakse uuesti.
def text_changed(*args):
    for kast in kastid:
        kast.destroy()
    tee_kastid_otsi()

koostisosad=['White Rum', 'Sugar Syrup', 'Lime Juice', 'Gin', 'Dry Vermouth', 'Bourbon', 'Angostura Bitters', 'Orange Bitters', 'Citrus Vodka', 'Triple Sec', 'Cranberry Juice', 'Cachaca', 'Vodka', 'Coffee Liqueur', 'Cream', 'Milk', 'Pineapple Juice', 'Coconut Cream', 'Sweet Red Vermouth', 'Campari', 'Créme de Mure', 'Lemon Juice', 'Tequila', 'Simple Syrup', 'Dark Rum', 'Anejo Rum', 'Cola', 'Rye Whiskey', 'Absinthe', ' Peychauds Bitters', 'Peppered Vodka', 'Sweet Vermouth', 'Tomato Juice', 'Tobasco sauce', 'Salt', 'Pepper', 'Gomme syrup', 'Light Rum', 'Orgeat Syrup', 'Amaretto', 'Egg-White', 'Cherry Heering', 'Benedictine', 'Soda Water', 'Chambord', ' Pineapple Juice', 'Vanilla Vodka', 'Kahlua', 'Bacardi Rum', 'Strawberry Liqueur', 'Lime juice', 'Caorunn Gin', 'Raspberry Syrup', 'Knob Creek Bourbon', 'Bourbon Whiskey', 'Apple Schapps', 'Brandy', 'Créme de Cacao', 'Pink Grapefruit Juice', 'Runny Honey', 'Scotch Whisky', 'Whiskey Liqueur', 'Pisco', 'Orange Juice', 'Champagne', 'Aged Rum', 'Creme de Banane', 'Creme de Mure', 'Orange Liqueur', 'Peach Schnapps', 'Créme de Cassis', 'Prosecco', 'Peach puree', 'Peach Bitters', 'Dry Sherry', 'Grapefruit Juice', 'Irish Cream Liqueur', 'freshly squeezed Orange Juice', 'Cognac', 'Double Cream', 'Raspberry Liqueur', 'Egg White', 'Scotch Whiskey', 'Maraschino Liqueur', 'Vanilla Sugar Syrup', 'Premium Gin', 'Lime Cordial', 'Baileys Cream Liqueur', 'Citron Vodka', 'Elderflower Cordial', 'Passoa', ' Lemon Juice', 'Grapefruit Soda', 'Squeezed Lemon Juice', 'Golden Rum', '151 Rum', 'Falernum', 'of Soda Water', 'Raspberry Vodka', 'Black Raspberry Liqueur', ' Cranberry Juice', 'Yellow Chartreuse', 'Blue WKD', 'Port', ' Black Raspberry Liqueur', 'Melon Liqueur', 'Sweet and Sour mix', 'Lemon and Lime Soda', 'Drambuie', 'Grapefruit Bitters']
#koostisosad=['Tequila', 'White Rum', 'Sugar Syrup', 'Lime Juice', 'Dry Vermouth', 'Gin', 'Sugar']

#MAIN
main=Tk()
main.title("cocktail time")
main.resizable(False, False)
#main.geometry("600x240")

#RAAM KUS SEES ON CHECKBOXID,LABEL
raam=Canvas(main,bg="lavender")
raam.grid()

#vaheraam
vaheraam=Frame(raam,bg="lavender")
vaheraam.grid(column=2,rowspan=20, sticky="n")


#parempoolne raam
#see on retsepti, pildi jne jaoks
retseptiraam=Frame(raam,bg="lavender")
retseptiraam.grid(column=3,row=0,rowspan=40,sticky="ne")

joogikoostisosad=Label(retseptiraam,text="the ingredients necessary for your drink:",bg="lavender")
joogikoostisosad.grid(column=3,row=0,sticky="nw")

tühi=Label(retseptiraam,text="",bg="lavender")#loll lahendus, aga ma olengi loll~
tühi.grid(column=3,row=1,sticky="nw")

joogiretsept=Label(retseptiraam,text="the recipe for your drink:",bg="lavender")
joogiretsept.grid(column=3,row=2,sticky="nw")






#LABEL "Mis koostisosad sul olemas on?"
silt=Label(raam,text="what ingredients do you currently have?",background="lavender")
silt.grid(row=0, sticky="w")

#SEARCHBOX
tk_name = StringVar()
tk_name.trace("w",callback=text_changed)
sisend = Entry(raam, textvariable=tk_name)
sisend.grid(row=1)


misJooki = Label(vaheraam, text="what are you feeling?", background="lavender")
misJooki.grid(row=0,sticky="n")

lb=Listbox(vaheraam,height=20)
lb.grid()


#print(anna_joogid())




tee_kastid_otsi()

main.mainloop()











