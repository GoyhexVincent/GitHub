import feedparser as fp
import time

#http://www.4imn.com/top200/# Lien utile vers les 200 plus gros journaux au monde.


#d = fp.parse('http://www.reddit.com/r/python/.rss')
#d = fp.parse ('http://www.theguardian.com/world/rss')
c = fp.parse('http://rss.nytimes.com/services/xml/rss/nyt/World.xml')
d = fp.parse('http://rss.lemonde.fr/c/205/f/3052/index.rss')
#d = fp.parse('http://mix.chimpfeedr.com/eaebb-rss-feed-try')
print (d ['feed']['title']) #titre
print (d ['feed']['link'])  #url
print (d.feed.subtitle)     #descriptif du feed.
print(len(d['entries']))    #combien de posts?
print(d['entries'][0]['title']) #titre du post 0.
print (d.entries[0]['link'])#recuperer le lien de chaque entry.
print (d.version)           #recuperer le type et la version du feed
print (d.headers)           #acces aux headers HTTP
print (d.headers.get('content-type'))
print (d.headers['Date'])   #date générale du feed, en gros l'heure actuelle à l'endroit ou se trouve le serveur.
print (d['entries'][0]['published']) #date du post.

feeds_to_parse=open("D:/Documents/goyhex/Privé/feedparser/feedparser_entry_tests_world.txt","r")

    
print ('\a'*60)
#Récuperer la liste des titres.
for line in feeds_to_parse:
    print (line)
    print ('\a'*60)
    parser = fp.parse(str(line))
    x = len(parser['entries'])
    count = 0
    while count < x: 
        print(' \a'+ parser['entries'][count]['title']+'; '+parser['entries'][count]['published'])
        count = count +1
    print ('\a'*60)
        

###Recuperer chaque post et leur liens associés.
##for post in d.entries:
##    print ('\a'+ post.title+':'+post.link)


feeds_to_parse.close()
