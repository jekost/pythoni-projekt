from bs4 import BeautifulSoup
import requests
import urllib.request



"""
url =
https://www.socialandcocktail.co.uk/top-100-cocktails/

sait=requests.get(url)
#sait=sait.read()

a=(sait.text)

kama=open("kama.txt","w")
kama.write(a)
kama.close()

def kirjuta_html_yles(url):
    try:
        u2 = urllib.request.urlopen(url)
    except:
        return False
    #salvesta html kohalikku arvutisse
    with open("tekst.txt","w") as tekst:
        for lines in u2.readlines():
            tekst.write(str(lines)+"\n")
    tekst.close()


#otsi kõik koostisosad kokteili leheküljelt(muuda ära et otsiks ingr.+retsept+...) #tekst.txt
def leia_koostiosad(fail):
    with open (fail) as tekst:
        soup=BeautifulSoup(tekst, "html.parser")
    output=soup.get_text()
    joogid=soup.find("h3",string="The Ingredients").next_sibling.next_sibling
    joogid=joogid.text
    return joogid
"""

#leia_koostisosad aga paned doci stringina
def leia_osad(url):
    global soup
    u2 = urllib.request.urlopen(url)
    doc=str(u2.readlines())
    soup=BeautifulSoup(doc,"html.parser")
    koostisosad=soup.find("h3",string="The Ingredients").next_sibling.next_sibling
    koostisosad=koostisosad.text
    return koostisosad

#leia retsept
def leia_retsept():
    retsept=soup.find("h3",string="The Ingredients").next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
    retsept=retsept.text
    return retsept

#leia pilt!:D
def leia_pilt():
 retsept=soup.find(property="og:image")
 return(retsept["content"])



#kama on tekstifail, kus on terve kokteilide emalehekülg välja salvestatud
with open ("kama.txt") as kama:
    soup=BeautifulSoup(kama, "html.parser")
output=soup.get_text()

joogid=soup.find_all("h3") #h3 tagi all on ainult joogid, ning üksikul juhul midagi muud
n=1
for jook in joogid:
    
    #exception handler üksikel juhtudel
    lopp=jook.text.replace(" ","-").replace("`","").lower() #muuda formaat Sellises't selliseks
    if lopp=="manhattan":
        lopp="manhatten"
    if lopp=="cuba-libre":
        lopp="cuba-libra"
    if lopp=="hen-parties":
        continue
    if lopp=="kir-royale":
        lopp="kir-royal"
    if lopp=="volcano":
        lopp="flaming-volcano"
    if "you-bring" in lopp:
        break

    print(str(n)+". ",jook.text) #prindi jooginimi

    url=("https://www.socialandcocktail.co.uk/cocktails/"+lopp)
    print("  ",leia_osad(url),"\n")
    print("  ",leia_retsept(),"\n")
    print("  ",leia_pilt(),   "\n")


    n+=1

