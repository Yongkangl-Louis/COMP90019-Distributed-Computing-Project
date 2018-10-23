#!/usr/bin/env python
# encoding: utf-8
# -------------------------------
# Yongkang Liu 849892
# this program is used harvest the tweets
# with the top 100 people user_id
# -------------------------------
import tweepy
import csv

consumer_key = "5l2pX84qjCvNPMLIBLl48aAfM"
consumer_secret = "Q3MNBvvPMheIhxLK4W8KRrvZ3YSaOXzgMTOzqjLs73nrwjLRCw"
access_token = "992003107230892032-z3xBOVIburBxImM7zmSP0AkjEHzw0c6"
access_secret = "SRLfPKZdjsBAXk06jdnjUuUZaiy9FQkmgQ8ksswEfbfVC"


def get_all_tweets(user_id):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (500 is the maximum allowed count)
    new_tweets = api.user_timeline(user_id=user_id, count=500)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(user_id=user_id, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[ tweet.id_str, tweet.created_at, tweet.coordinates] for tweet in alltweets]

    # write the csv
    with open('/Users/liuyongkang/Downloads/test/venv/top10 user coordinates/10.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["tweet_id", "created_at", "coordinates"])
        writer.writerows(outtweets)
pass


if __name__ == '__main__':
    with open('/Users/liuyongkang/Downloads/test/venv/top100CoordinatesTweetsPeople.csv', 'r') as f:
        ID = csv.reader(f)
        for row in ID:
            try:
                get_all_tweets('16539819')
            except tweepy.TweepError as e:
                print('Failed to run the command on that user, Skipping...')
            except IndexError as e:
                print('List index out of range, Skipping...')
                continue
