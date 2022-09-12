import urllib3
import json


# Get Ghibli data from Ghibli API
http = urllib3.PoolManager()
r = http.request('GET', 'https://ghibliapi.herokuapp.com/films')
json_film = json.loads(r.data.decode('utf-8'))

