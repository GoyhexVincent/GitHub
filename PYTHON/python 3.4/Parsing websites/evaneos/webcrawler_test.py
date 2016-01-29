#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import re
import datetime
import time


#   EVANEOS:
#Structure du site:
#Lv1: "evaneos.com/ou-partir/    #Parser ici le nom de chaque type de circuit
#Lv2: "evaneos.com/ou-partir/"+link+"/circuit" #Ici les destinations proposées
#Lv3: PAGE A PARSER, récuperer les noms de chaque lieux du circuit.  #Ici le détail des lieux pour chaque destination.
#------------------------------------------------------------------
#Une fois que cette tache est effectuée, voir le second script qui aura
#Pour but de récuperer via googlemaps/googleNLP les Lat/Long de chacun des lieux contenus dans les circuits.
#Dans l'idéal, créer un geojson par circuit directement, sinon d'abord un csv puis encore un script pour passer en geojson.
#Enfin, place à D3.js pour faire une dataviz digne de ce nom.


try:
    with open("index_lv1_1.txt", "w", encoding="utf-8") as Index_lv1:
        with open("index_lv2_2.txt", "w", encoding="utf-8") as Index_lv2:
            with open("index_lv3_3.txt","w", encoding="utf-8") as Index_lv3:
                starting_point = datetime.datetime.now()
                print(starting_point)
            
                #LV1

                url = 'http://www.evaneos.com/ou-partir/'  
                headers = {}
                headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i 686) AppleWebKit/537.'
                
                req = urllib.request.Request(url, headers=headers)
                resp = urllib.request.urlopen(req)
                respData = resp.read()
                links_lv1 = re.findall(r'</h2></a><a href="(.*?)" title="', str(respData))
                for link_lv1 in links_lv1:
                    #print(link_lv1)
                    Index_lv1.write(str(link_lv1)+'\n')
                    
                    #LV2

                    try:
                        url = link_lv1+'/circuit/'  
                        req = urllib.request.Request(url, headers=headers)
                        resp = urllib.request.urlopen(req)
                        respData = resp.read()
                        links_lv2 = re.findall(r'<h2><a href="(.*?)"  data-tag="trackEvent" ', str(respData))
                        for link_lv2 in links_lv2:
                            #print(link_lv2)
                            Index_lv2.write(str(link_lv2)+'\n')

                            #LV3:
                            try:
                                url = link_lv2
                                req = urllib.request.Request(url, headers=headers)
                                resp = urllib.request.urlopen(req)
                                respData = resp.read()
                                links_lv3 = re.findall(r'class="link"  data-tag="trackEvent" data-parm1="Fiche_itineraire" data-parm2="poi_header_list" data-parm3="poi_link" >(.*?)</a>', str(respData),)
                                for link_lv3 in links_lv3:
                                    link_lv3 = [str(link_lv3)]
                                    print(link_lv3)
                                    link_lv3=str(link_lv3).encode('Latin1').decode('utf-8') #Petit souci au niveau de l'encodage ici, à corriger dès que possible.
                                    #print(link_lv3)
                                    Index_lv3.write(str(link_lv3))


                                
                            except Exception as e:
                                print(str(e))
                            
                    except Exception as e:
                        print(str(e))
            Index_lv2.close()
            Index_lv1.close()
            Index_lv3.close()
            print(datetime.datetime.now())
            print ('Il aura fallu: ' +str(datetime.datetime.now()-starting_point) + 'pour parser ce site.')


except Exception as e:
    print(str(e))
