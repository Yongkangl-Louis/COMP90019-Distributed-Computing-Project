# -------------------------------
# Yongkang Liu 849892
# this program is used to connect the view 'toptweets/tweets' in database
# then get the top 100 people tweets with coornidates
# -------------------------------
import json
import csv
from collections import Counter
import couchdb
import numpy as np


couch = couchdb.Server('http://admin:password@115.146.85.196:5984/')
data1 = couch['distance']

result = data1.view('topuser/distance')
tweet_content = []
for item in result:
    tweet_content.append(item.value)


a = np.array(tweet_content)
count = Counter(a).most_common(100)

with open('/home/ubuntu/code/top100CoordinatesTweetsPeople.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(["user_id", "tweets_count"])
    for row in count:
        writer.writerow(row)



