import cookiejar
import urllib
import datetime
import requests
import json

default = 'c200a942-a4a3-426f-a7a6-4cbc20316d7a'
token = '30c328c3-99fe-4429-bf02-4f91a7123915'


url = "http://api.navitia.io/v1/journeys?from=-122.4752;37.80826&to=-122.402770;37.794682&datetime=20140118T0800"
values = {
    'default': default,
    'token': token
          }

r = requests.post(url, data=values)
print (r.content)


url ='http://api.navitia.io:80'
r = requests.post(url, data = values)
print(r.content)
