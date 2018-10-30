#!/usr/bin/env bash

#install.
sudo apt-get update &> /dev/null
sudo apt-get install -y vim &> /dev/null
sudo apt-get -y install python-pip &> /dev/null
#--quiet
sudo pip install couchdb --quiet
sudo pip install cloudant --quiet
sudo pip install tweepy --quiet
sudo pip install afinn --quiet
echo "installed pakages for Harvester and analyser"

echo "starting deployment"
cd zip

sudo nohup python -u /home/ubuntu/code/mostFollower.py &> followers.out&
#wait for 30 sec
sleep 30
sudo nohup python -u /home/ubuntu/code/view_creation1.py &> view_creation1.out&
sudo nohup python -u /home/ubuntu/code/view_creation2.py &> view_creation2.out&
sudo nohup python -u /home/ubuntu/code/view_creation3.py &> view_creation3.out&
sudo nohup python -u /home/ubuntu/code/mostFollower.py &> mostFollower.out&
sudo nohup python -u /home/ubuntu/code/getMostFollower.py &> getMostFollower.out&
sudo nohup python -u /home/ubuntu/code/mostTweets.py &> mostTweets.out&
sudo nohup python -u /home/ubuntu/code/getMostTweets.py &> getMostTweets.out&
sudo nohup python -u /home/ubuntu/code/distance1.py &> distance1.out&
sudo nohup python -u /home/ubuntu/code/distance2.py &> distance2.out&
sudo nohup python -u /home/ubuntu/code/harvester.py &> harvester.out&

echo "updating data to database"

(curl -d "@twitter.json" -H "Content-Type: application/json" -X POST http://115.146.85.196:5984/twitter) &> /dev/null

sudo nohup python -u /home/ubuntu/zip/view_creation3.py &> view_creation3.out&

echo "done with restarting..."



