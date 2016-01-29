import feedparser as fp
import re
import datetime
import urllib3
import urllib.request as req
## proxy = req.ProxyHandler({'http':'proxy.brgm.fr:8080' }) C'est pas pour toi ça
#http://www.4imn.com/top200/# Lien utile vers les 200 plus gros journaux au monde.

starting_point = datetime.datetime.now()
with open('D:/Documents/goyhex/Privé/feedparser/SHP_world_countries_RSS.csv','r') as world_countries:          
    for line in world_countries:
        with open('D:/Documents/goyhex/Privé/feedparser/feedparser_entry_tests_world.txt','r') as feeds_to_parse:
            for line2 in feeds_to_parse:
                #print ('\a'*60)
                if line !='':
                    country_name = re.compile("(?<=\"\D)(.*)(?=\"\"\;)")
                    country_geom = re.compile("(?<=\"\;\"\")(.*)(?=\"\"\")")
                    match_country = re.findall(country_name,line)
                    #print(match_country)
                    match_geom = re.findall(country_geom,line)
                
                    #print (match_country)
                    if line2 !='':
                        #print (line2)
                        #print ('\a'*60)
                        # parser = fp.parse(str(line2),handlers = [proxy])
                        parser = fp.parse(str(line2))
                        x = len(parser['entries'])
                        count = 0
                        while count < x: 
                            entry_title = parser['entries'][count]['title']
                            entry_url = parser['entries'] [count] ['link']
                            
                            entry_country = re.compile(match_country[0])
                            entry_country_result = re.findall(entry_country,entry_title)
                            #print(entry_country_result)
                            #print(entry)
                            count = count +1
                            if entry_country_result:
                                print(entry_country_result[0] + ' ; ' + entry_title)
    print('\a'*60)
    print(datetime.datetime.now())
    print('Il aura fallu: ' + str(datetime.datetime.now()-starting_point)+ 'pour traiter les flux RSS d\'aujourd\'hui')
    





##with open('D:/Documents/goyhex/Privé/feedparser/SHP_world_countries_RSS.csv','r') as world_countries:
##    for line in world_countries:
##        country_name = re.compile("(?<=\"\D)(.*)(?=\"\"\;)")
##        country_geom = re.compile("(?<=\"\;\"\")(.*)(?=\"\"\")")
##        match_country = re.findall(country_name,line)
##        match_geom = re.findall(country_geom,line)
##        print (match_geom)
