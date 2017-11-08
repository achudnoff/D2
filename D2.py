# python 3

import requests
import json
import csv


#Configs
apiKey = '12ca3cea17d843c2a1ffbb4348df2a4e'
apiURL = 'https://www.bungie.net/Platform'
apiEndpoint = '/User/SearchUsers'

resp = requests.get(apiURL+apiEndpoint, headers = {'X-API-Key' : apiKey}, params = {'q' : 'GigaPeon'})

apiEndpoint = '/Destiny2/Stats/Leaderboards/Clans/849799/'

resp = requests.get(apiURL+apiEndpoint, headers = {'X-API-Key' : apiKey}, params = {'maxtop' : 99999, 'modes' : 39})

results = json.loads(resp.text)

output = csv.writer(open("test.csv", "wb+"))

print (json.loads(resp.text))

file = open("testfile.txt", "w")
file.write (resp.text)