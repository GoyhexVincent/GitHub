# encoding: utf-8
#
# JCDecaux
# http://developer.jcdecaux.com/
#

# update options
#   api_key : JCDecaux API key (required)

import urllib.request as req
import json
import sys
import codecs


reader = codecs.getreader("utf-8")
# cities = { 'local name' : {
#    'country'  : (2 letters ISO 3166)' }}
# the local name is the one displayed beside the map
# see http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
cities = {
    u'Amiens'             : { 'country': 'FR' } ,
    u'Besancon'           : { 'country': 'FR' } ,
    u'Bruxelles-Capitale' : { 'country': 'FR' } ,
    u'Cergy-Pontoise'     : { 'country': 'FR' } ,
    u'Créteil'            : { 'country': 'FR' } ,
    u'Göteborg'           : { 'country': 'SE' } ,
    u'Ljubljana'          : { 'country': 'SI' } ,
    u'Luxembourg'         : { 'country': 'LU' } ,
    u'Lyon'               : { 'country': 'FR' } ,
    u'Marseille'          : { 'country': 'FR' } ,
    u'Mulhouse'           : { 'country': 'FR' } ,
    u'Namur'              : { 'country': 'BE' } ,
    u'Nancy'              : { 'country': 'FR' } ,
    u'Nantes'             : { 'country': 'FR' } ,
    u'Paris'              : { 'country': 'FR' } ,
    u'Rouen'              : { 'country': 'FR' } ,
    u'Santander'          : { 'country': 'ES' } ,
    u'Sevilla'            : { 'country': 'ES' } ,
    u'Stockholm'          : { 'country': 'SE' } ,
    u'Toulouse'           : { 'country': 'FR' } ,
    u'富山市'             : { 'country': 'JP' } ,
    u'Valencia'           : { 'country': 'ES' }
}

# Unused for now
info = {
    'provider' : 'JCDecaux',                               # name of the data provider
    'info_url' : '',                                       # where to get info (users) where applicable
    'dev_info_url' :  'http://developer.jcdecaux.com/' ,   # where to get more info (developers)
    'logo_filename' :  ''                                  # logo file which should be located under
                                                           # static/imgs/logos
}

_provider_ids = {
    u'Amiens'             : 'Amiens',
    u'Besancon'           : 'Besancon',
    u'Bruxelles-Capitale' : 'Bruxelles-Capitale',
    u'Cergy-Pontoise'     : 'Cergy-Pontoise',
    u'Créteil'            : 'Creteil',
    u'Göteborg'           : 'Goteborg',
    u'Ljubljana'          : 'Ljubljana',
    u'Luxembourg'         : 'Luxembourg',
    u'Lyon'               : 'Lyon',
    u'Marseille'          : 'Marseille',
    u'Mulhouse'           : 'Mulhouse',
    u'Namur'              : 'Namur',
    u'Nancy'              : 'Nancy',
    u'Nantes'             : 'Nantes',
    u'Paris'              : 'Paris',
    u'Rouen'              : 'Rouen',
    u'Santander'          : 'Santander',
    u'Sevilla'            : 'Seville',
    u'Stockholm'          : 'Stockholm',
    u'Toulouse'           : 'Toulouse',
    u'富山市'             : 'Toyama',
    u'Valencia'           : 'Valence'
}



print('Voici les villes disponibles:', cities)
print('-'*50)
print ('Il ne reste pour vous qu\'a choisir la ville, rentrer son nom dans la fonction update(city) et croiser les doigts.')





def update(city):
    """Download the data for each cities, storing it in json format in data/<name>.json
    It should be an array of dicts, each with the following keys:
        id              : (int) the ID of the station, must be unique for the city
        name            : (string) the name of the station (usually tied to location)
        position        : (dict) a dict with 'lat' and 'lng' keys, the latitude and longitude, as floats
        open            : (bool) whether the station is available
        bike_stands     : (int) the total number of stands, or docks, available at this station
        available_bikes : (int) the number of bikes available at this station
        last_update     : (int) the unix time of the last data update, in msecs
    """
    api_key ='ff50b914028a6778644181aecc1fa491077f4100'
    if api_key:
        c_info_url_format = "https://api.jcdecaux.com/vls/v1/stations?contract={0}&apiKey="+api_key

        if city:
            url = c_info_url_format.format(_provider_ids[city])
            try:
                r = req.urlopen(url)
                in_json  = json.load(reader(r))
                out_json = _reformat_json(in_json, city)
                with open('jcdecaux.json'.format(city).encode('utf-8'), 'w') as f:
                    json.dump(out_json, f, separators=(',',':'));
            except Exception as e:
                print(str(e))
    else:
        sys.stderr.write('JCDecaux API key not defined in options dict')
def _reformat_json(data, city):
    stations = []
    for s in data:
        try:
            position = { 'lat' : round(s['position']['lat'], 6), 'lng' : round(s['position']['lng'], 6) }
        except:
            if 'name' in s:
                sys.stderr.write('Coordinates for station "{0}" ({1}) could not be parsed, it will not show on the map\n'.format(s['name'], city))
            else:
                raise KeyError
            position = { 'lat' : 0, 'lng' : 0 }
        station = {
            'id'              : s['number'],
            'name'            : s['name'],
            'position'        : position,
            'open'            : s['status'] == 'OPEN',
            'bike_stands'     : s['bike_stands'],
            'available_bikes' : s['available_bikes'],
            'last_update'     : s['last_update']
        }
        stations.append(station)
    return stations
                

