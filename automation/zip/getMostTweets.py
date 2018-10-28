# -------------------------------
# Yongkang Liu 849892
# this program is used to connect the view 'toptweets/tweets' in database mosttweets
# then sort by 'tweets_count' output csv with user_ID and tweets_count
# -------------------------------


from collections import Counter
import couchdb
import numpy as np
import json
import csv

couch = couchdb.Server('http://admin:password@115.146.85.196:5984/')
data1 = couch['mosttweets']

result = data1.view('toptweets/tweets')
numberofID = []
for row in result:
    numberofID.append(row.value)

a = np.array(numberofID)
count = Counter(a).most_common(30)

with open('/home/ubuntu/code/top10MostTweets.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(["user_id", "tweets_count"])
    for row in count:
        writer.writerow(row)

