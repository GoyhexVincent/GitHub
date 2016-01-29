# -*- coding: utf-8 -*-	
import time
import urllib2
from urllib2 import urlopen
import re
import cookielib, urllib2
from cookielib import CookieJar
import datetime
 
 
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
 
def main(max_pages):
    f = open('output_crus.txt','a')

    
    page=2
    while page< max_pages:
        
        try:
                        url = 'http://www.crus.fr/index.php?type_rub=vins&recherche=Rechercher%20un%20vin&prix=&annee=&couleur=&page=0'+str(page)
            sourceCode = opener.open(url).read()
            #print sourceCode
 
            try:
                #titles = re.findall(r'\" title="(.*?)">',sourceCode)
                links = re.findall(r'<a class="plus_infos_prod" href="(.*?)">Fiche produit</a>',sourceCode)
                for link in links:
                    print ('http://www.crus.fr/'+ link +'\n' )
                    url2 = link
                    sourceCode2 = opener.open('http://www.crus.fr/'+ url2).read()
                    #print(sourceCode2)
                    annee = re.findall(r'<strong><span itemprop="datePublished" content="(.*?)">',sourceCode2)
                    film = re.findall(r'og:title" content="(.*?)" /><meta',sourceCode2)
                    
                    #f.write(film[0] +';'+annee[0]+';'+'horreur'+'\n') # python will convert \n to os.linesep #horreur
                    f.write(film[0] +';'+annee[0]+';'+'science-fiction'+'\n') # python will convert \n to os.linesep #syfy
                #for link in links:
                    #print link
            except Exception, e:
                print str(e)
    
        except Exception,e:
            print str(e)
            pass
        page +=1
    f.close()

        
        
 
print('ecrivez "main(x)", remplacez x par le nombre de page Ã  parser Ã  la suite')



    

    
    
