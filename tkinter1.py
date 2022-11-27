from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#def otsi_komponente():
koostisosad=[
    "Tequila",
    "Sugar",
    "Rum",
    "Soda"
]

raam=Tk()
raam.title("cocktail time")
raam.geometry("600x400")

#LABEL "Mis koostisosad sul olemas on?"
silt=ttk.Label(raam,text="Mis koostisosad sul olemas on?")
silt.grid(row=1)

#CHECKBOXES
koostisosa_nupp_value={}
for koostisosa in koostisosad:
    koostisosa_nupp_value[koostisosa]=False


print(koostisosa_nupp_value)
n=1
for koostisosa in koostisosad:
    n+=1
    Checkbutton(raam, text=koostisosa, variable=koostisosa_nupp_value[koostisosa]).grid(row=n, sticky=W)



raam.mainloop()





