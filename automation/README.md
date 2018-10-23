### Deployment
The follows package need to be preinstalled. <br>

* ansible <br>
* boto2 <br>
* python3 <br>
* rpl: used to replaces strings with new strings in multiple text files. <br>
(https://github.com/kcoyner/rpl) <br>

The security rules need to support ssh (port 22) and CouchDB (port 5984). <br>

The private key and OpenStack user credential are needed. <br>
 
Use the command：<br>
$ python start.py       <br>

Two virtual machines will be set up, the IP address can be found in file “host”. <br>
