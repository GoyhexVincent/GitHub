import urllib.request
import urllib.parse
import re

# URLS
url = 'http://handiman.univ-paris8.fr/~isis/ens/'
values = {'s':'basics',
          'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)

respData = resp.read()

print(respData)

#Parse out paragraph data:
#Use of regular expressiosn to go through the 'junk' we got from our url

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
for eachP in paragraphs:
    #print(eachP)
    print('is this working?')
    #The result we get is the successfull parse of the content located between <p> </p> of one URL.

