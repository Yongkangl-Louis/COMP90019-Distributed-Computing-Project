# -------------------------------
# Yongkang Liu 849892
# creat database named distance
# filter the field of user_ID and coordinates to database 
# -------------------------------

import tweepy
import json
import sys
import couchdb

#database name and server url
database_server = 'http://user:password@115.146.85.196:5984/'
couch = couchdb.Server(database_server)

database_name ='distance'
if database_name in couch:
    database = couch[database_name]
else:
    database = couch.create(database_name)


with open('home/ubuntu/code/twitter.json', 'r') as f:

    for line in f:
        try:
            line = line.rstrip(',\n\r')
            data = json.loads(line)
            doc = data['doc']
            user_id = doc['user']['id']
            coordinates = doc['coordinates']['coordinates']
            doc1 = {'user_id': user_id, 'coordinates':coordinates}
            database.save(doc1)
        except:
            continue

