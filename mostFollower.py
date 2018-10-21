from __future__ import unicode_literals
import tweepy
from tweepy import API
import json
import csv
import codecs
import unicodedata
import sys
import operator
import itertools

access_token = "5l2pX84qjCvNPMLIBLl48aAfM"
access_token_secret = "Q3MNBvvPMheIhxLK4W8KRrvZ3YSaOXzgMTOzqjLs73nrwjLRCw"
consumer_key = "992003107230892032-z3xBOVIburBxImM7zmSP0AkjEHzw0c6"
consumer_secret = "SRLfPKZdjsBAXk06jdnjUuUZaiy9FQkmgQ8ksswEfbfVC"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


with open('/Users/mushroom/PycharmProjects/project1/venv/twitter_data.csv','r') as f:
    reader = csv.reader(f, delimiter=',')
    table =[]
    header  = f.readline()
    for line in f:
        col = line.split(',')
        col[1] = int(col[1][:])
        table.append(col)
    sortedlist = sorted(table, key = lambda x:int(x[1]), reverse = True)

    with open('/Users/mushroom/PycharmProjects/project1/venv/mostFollowers.csv', 'w') as f1:
        writer = csv.writer(f1, delimiter=',')
        writer.writerow(["user_id", "followers"])
        writer.writerows(sortedlist)

    l2 = []
    l2.append(sortedlist[0])
    for data in sortedlist:
        k=0
        for item in l2:
            if data[0] != item[0]:
                k+=1
            else:
                break
            if k==len(l2):
                l2.append(data)

    with open('/Users/mushroom/PycharmProjects/project1/venv/mostFollowers_noduplicate.csv', 'w') as f2:
        writer2 = csv.writer(f2, delimiter=',')
        writer2.writerow(["user_id", "followers"])
        writer2.writerows(l2)








