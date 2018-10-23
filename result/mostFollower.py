# -------------------------------
# Yongkang Liu 849892
# creat database named mostfollowers
# filter the field of user_ID and followers_count to database
# -------------------------------

import tweepy
import json
import sys
import couchdb

#connect to database
database_server = 'http://user:password@127.0.0.1:5984/'
couch = couchdb.Server(database_server)

database_name ='mostfollowers'
if database_name in couch:
    database = couch[database_name]
else:
    database = couch.create(database_name)

# keep the field of user_ID and followers_count
with open('/Users/mushroom/PycharmProjects/test/venv/twitter.json', 'r') as f:

    for line in f:
        try:
            line = line.rstrip(',\n\r')
            data = json.loads(line)
            doc = data['doc']
            user_id = doc['user']['id']
            followers = doc['user']['followers_count']
            doc1 = {'user_id': user_id, 'followers':followers}
            database.save(doc1)
        except:
            continue

