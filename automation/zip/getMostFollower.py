# -------------------------------
# Yongkang Liu 849892
# this program is used to connect view of 'topfollowers/followers' in database mostfollowers
# then sort by 'followers_count' output csv with user_ID and most followers
# -------------------------------


import couchdb
import csv

couch = couchdb.Server('http://admin:password@115.146.85.196:5984/')
data1 = couch['mostfollowers']

table =[]
for item in data1.view('topfollowers/followers', descending=True, limit=100):
    table.append(item.value)

l1 = []
l1.append(table[0])
for data in table:
    k=0
    for item in l1:
        if data[0] != item[0]:
            k+=1
        else:
            break
        if k==len(l1):
            l1.append(data)
l2 =l1[:11]

with open('/home/ubuntu/code/top10MostFollowers.csv', 'w') as f2:
    writer2 = csv.writer(f2, delimiter=',')
    writer2.writerow(["user_id", "followers"])
    for row in l2:
        writer2.writerow(row)

