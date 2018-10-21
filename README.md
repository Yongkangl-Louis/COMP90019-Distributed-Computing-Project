### COMP90019-Distributed-Computing-Project

Master of Information Technology <br> 
COMP90019 Distributed Computing Project <br> 
25 Point Research Project  2018 <br> 

### A Research of Social Media User Behaviour Using Twitter Data of Melbourne <br> 

Supervisor: Professor Richard Sinnott <br> 
Student Name: Yongkang Liu <br> 

#### The implementation of the project.

### automation
>>Deployement of Ansible. <br>
>>Code used for analysis. <br>

### result
>>Code used to analysis data <br>
>>Output file <br>

### Deployment
The follows package need to preinstalled. <br>

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


