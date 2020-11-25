#-------------------------------------------------------------------------------
# Name:        My IP
# Purpose:
#
# Author:
#
# Created:     15.05.2020
# Copyright:   (c)  2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import json
import requests

url = 'http://ru.sxgeo.city/json/'
page = requests.get(url + '')
data = json.loads(page.text)
city = data['city']['name_en']
iso = data['country']['iso']
my_ip = data['ip']
print (my_ip + '   ' + iso + '   ' + city)

