import urllib3
import json


# Get Ghibli data from Ghibli API Heroku app 
http = urllib3.PoolManager()
r = http.request('GET', 'https://ghibliapi.herokuapp.com/films')
json_film = json.loads(r.data.decode('utf-8'))

# Dump Data from Ghibli API 

with open("film_info.json", "w") as outfile: 
    json.dump(json_film, outfile)