import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
    print(output)

def tee_kastid():
    rida = 1
    global kastid
    kastid = {}
    for koostisosa in range(len(koostisosad)):
        nimi = koostisosad[koostisosa]
        rida += 1
        current_var = IntVar()
        #######
        current_box = Checkbutton(raam, text=nimi, variable=current_var, background="lavender", command=tagasta)
        current_box.grid(row=rida, sticky=W)
        current_box.var = current_var
        kastid[current_box] = nimi

def tee_kastid_otsi():#teeb ainult need kastid kus on sõne sees ("u"->"Rum","Sugar")
    sõne=tk_name.get()
    rida = 1
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
        current_box.grid(row=rida, sticky=W)
        current_box.var = current_var
        kastid[current_box] = nimi

def text_changed(*args):
    print( tk_name.get() )
    for kast in kastid:
        kast.destroy()
    tee_kastid_otsi()

koostisosad=[
    "Tequila",
    "White Rum",
    "Sugar Syrup",
    "Lime Juice",
    "Dry Vermouth",
    "Gin",
    "Sugar",
    "Bourbon/American Whiskey",
    "Ice",
    "Cola",
    "Light Beer",
    "Cocoa Butter",
    "Tere",
    "Scotch/Scottish Whiskey",
    "Irish Whiskey"
    ]


#MAIN
main=Tk()
main.title("cocktail time")
#main.geometry("600x240")

#RAAM KUS SEES ON CHECKBOXID,LABEL
raam=Canvas(main,bg="lavender")
raam.grid(sticky="n,e,w,s")

#vaheraam
vaheraam=Frame(raam)

#LABEL "Mis koostisosad sul olemas on?"
silt=ttk.Label(raam,text="Mis koostisosad sul olemas on?",background="lavender")
silt.grid(sticky="w")

#SEARCHBOX
tk_name = StringVar()
tk_name.trace("w",callback=text_changed)
sisend = Entry(raam, textvariable=tk_name)
sisend.grid()



#SCROLLWHEEL
#scroll=Scrollbar(raam, command=raam.yview)
#scroll.grid(sticky="n,e,s",rowspan=10)
#raam["yscrollcommand"]=scroll
#raam.configure(scrollregion=raam.bbox("all"))

#scroll.config( command = raam.yview )


tee_kastid()

main.mainloop()










