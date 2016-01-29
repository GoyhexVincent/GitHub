import feedparser as fp
import time
import datetime
import psycopg2
import urllib3
import urllib.request as req
import re


def dbconnection():
    conn_string ="host='localhost' dbname='postgres' user='postgres' password='1234567' port='5432'"
    print ("Connecting to dababase\n ->%s" %(conn_string))

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        print ("Connected!\n")
    except:
        print ('Unable to connect to the database milord')       

    #def collectFeed():
    starting_point = datetime.datetime.now()
    with open('D:/Documents/goyhex/Privé/feedparser/SHP_world_countries_RSS.csv','r') as world_countries:          
        for line in world_countries:
            with open('D:/Documents/goyhex/Privé/feedparser/feedparser_entry_tests_world.txt','r') as feeds_to_parse:
                for line2 in feeds_to_parse:
                    if line !='':
                        country_name = re.compile("(?<=\"\D)(.*)(?=\"\"\;)")
                        country_geom = re.compile("(?<=\"\;\"\")(.*)(?=\"\"\")")
                        match_country = re.findall(country_name,line)
                        match_geom = re.findall(country_geom,line)
                        if line2 !='':
                            # parser = fp.parse(str(line2),handlers = [proxy])
                            parser = fp.parse(str(line2))
                            x = len(parser['entries'])
                            count = 0
                            while count < x: 
                                entry_title = parser['entries'][count]['title']
                                entry_url = parser['entries'] [count] ['link']                           
                                entry_country = re.compile(match_country[0])
                                entry_country_result = re.findall(entry_country,entry_title)
                                count = count +1          
                                if entry_title != cursor.execute("SELECT public.feed.title FROM public.feed "):
                                    if entry_country_result:
                                        cursor.execute("INSERT INTO feed (link, title, publication_date, newspaper, country) VALUES (%s, %s, %s, %s, %s)",
                                            (entry_url, entry_title,parser['entries'][count]['published'],parser['feed']['title'],entry_country_result[0]))
                                        conn.commit()
                                        print(entry_title)

dbconnection()
print('\a'*60)
print(datetime.datetime.now())
print('Il aura fallu: ' + str(datetime.datetime.now()-starting_point)+ 'pour traiter les flux RSS d\'aujourd\'hui')
    

                                
##CREATE TABLE feed (
##id SERIAL,
##link varchar, 
##title varchar, 
##publication_date date, 
##newspaper varchar,
##country varchar
##);


























