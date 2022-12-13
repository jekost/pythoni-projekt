
from luger import *
import wget
# ei soovita runida
pildi_nimed = dict()
for võti, sisu in retseptid.items():
    url = sisu[2]
    nimi = võti
    #file_name = wget.download(url)
    pildi_nimed[võti] = file_name

    print('Image Successfully Downloaded: ', võti)

print(pildi_nimed)

    
    
